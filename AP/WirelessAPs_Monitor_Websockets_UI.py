import os
import json
import time
from shutil import copyfile
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import websockets
import asyncio
from deepdiff import DeepDiff
import re
import logging
#import pdb


class FileHandler(FileSystemEventHandler):
    event_type = ''
    src_path = ''

    def on_modified(self, event):
        self.event_type = event.event_type
        self.src_path = event.src_path
        return


async def file_change_notification(websocket, acc_points_path, q):
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=acc_points_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(0.2)
            if event_handler.event_type == 'modified':
                await websocket.send('DEBUG:\tevent_type\t' + event_handler.event_type+'\tin\t'+'src_path\t' + event_handler.src_path)
                await q.put('modified')
                event_handler.event_type = ''
                acc_points_file = r'C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json'
                # A file which contains surrounding Wireless APs in JSON format after event triggered
                access_points_after_event_file = r'C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_after_event.json'
                # Copy json file after the event triggred
                copyfile(acc_points_file, access_points_after_event_file)
                await websocket.send("DEBUG:\tCopied json file after file modification\n")
                break
    except KeyboardInterrupt:
        observer.stop()
    return



async def json_compare(websocket, file1, file2):
    #pdb.set_trace()
    with open(file1) as f:
        data_load1 = json.load(f)
        data1 = data_load1['access_points']
        ord_data1 = sorted(data1, key=lambda item: item['ssid'])
    with open(file2) as f:
        data_load2 = json.load(f)
        data2 = data_load2['access_points']
        ord_data2 = sorted(data2, key=lambda item: item['ssid'])
    if ord_data1 == ord_data2:
        await websocket.send('\nDEBUG:\tWireless APs json file contents are same even after file changes')
    else:
        await websocket.send("\nDEBUG:\tWireless APs json file contnents are not same")
        data1_json = json.dumps(dict(enumerate(ord_data1)), indent=4)
        #await websocket.send('DEBUG:\tWireless APs in JSON format before event triggered:' + "\n" + data1_json)
        data2_json = json.dumps(dict(enumerate(ord_data2)), indent=4)
        #await websocket.send('\nDEBUG:\tWireless APs in JSON format after event triggered(after few seconds):' + "\n" + data2_json)
        #Checking difference of 2 json files
        ddiff = DeepDiff(data1_json, data2_json)
        diff_change = ddiff['values_changed']['root']['diff']
        data_lines = re.split("\n", diff_change)
        tmp_file = r'C:\Python37\MyScriptsSE\CodingExercise\AP\temp.txt'
        await write_diff_data_temp_file(data_lines, tmp_file)
        await websocket.send("\nDEBUG:\tDisplay surrounding Wireless APs: ")
        await read_diff_data_from_temp_file(websocket, tmp_file)
        await remove_temp_file(tmp_file)


async def write_diff_data_temp_file(data_lines, tmp_file):
    with open(tmp_file, "w+") as f:
        for data_line in data_lines:
            if re.search("ssid|snr|channel", data_line):
                data_line = data_line.replace(":", "")
                data_line = data_line.replace(",", "")
                f.write(data_line)
                f.write("\n")
        f.close()


async def read_diff_data_from_temp_file(websocket, tmp_file):
    with open(tmp_file, "r") as f:
        ssid_name = ""
        ssid_chk = ""
        AP_LEN = 3

        while True:
            line = f.readline()
            if line == "":
                break
            data_line = re.sub("\s+", " ", line)
            data_list = re.split(" ", data_line)
            data = data_list[:3]
            if data[1] == '"ssid"':
                ssid_name = data[2]
                AP_num = 1
                if data[0] == '':
                    ssid_chk = "ssid_rcvd"
                    continue
                if data[0] == '+':
                    ssid_chk = "ssid_added"
                    continue
                if data[0] == '-':
                    ssid_chk = "ssid_removed"
                    await websocket.send("\nINFO:\t" + ssid_name + ' is removed from the list')
                    continue

            if ssid_chk == "ssid_added":
                if data[0] == '+':
                    if data[1] == '"snr"':
                        snr_value = data[2]
                    if data[1] == '"channel"':
                        channel_value = data[2]
                    AP_num += 1
                    if AP_num == AP_LEN:
                        ssid_chk = ""
                        await websocket.send(
                                "\nINFO:\t" + ssid_name + ' is added to the list with ' + ' SNR ' + snr_value + ' and channel ' + channel_value)
                    continue

                if data[0] == '':
                    if data[1] == '"snr"':
                        snr_value = data[2]
                    if data[1] == '"channel"':
                        channel_value = data[2]
                    AP_num += 1
                    if AP_num == AP_LEN:
                        ssid_chk = ""
                        await websocket.send(
                                "\nINFO:\t" + ssid_name + ' is added to the list with ' + ' SNR ' + snr_value + ' and channel ' + channel_value)
                    continue

            if ssid_chk == "ssid_rcvd":
                if data[0] == '':
                    AP_num += 1
                    if AP_num == AP_LEN:
                        ssid_chk = ""
                    continue

                if data[0] == '-':
                    if '"snr"' == data[1]:
                        snr_old = data[2]
                    if '"channel"' == data[1]:
                        channel_old = data[2]
                    continue

                if data[0] == '+':
                    if data[1] == '"snr"':
                        snr_value = data[2]
                        await websocket.send(
                                "\nINFO:\t" + ssid_name + '\'s' + ' SNR has changed from ' + snr_old + ' to ' + snr_value)
                    if data[1] == '"channel"':
                        channel_value = data[2]
                        await websocket.send(
                                "\nINFO:\t" + ssid_name + '\'s' + ' channel has changed from ' + channel_old + ' to ' + channel_value)
                    AP_num += 1
                    if AP_num == AP_LEN:
                        ssid_chk = ""
                    continue
    f.close()

async def remove_temp_file (temp_file):
    if os.path.exists(temp_file):
        os.remove(temp_file)
    else:
        pass

async def logger(websocket, q):
    if await q.get() == 'modified':
        access_points_before_event_file = 'C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_before_event.json'
        access_points_after_event_file = 'C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_after_event.json'
        await json_compare(websocket, access_points_before_event_file, access_points_after_event_file)


async def monitor(websocket, path):
    #pdb.set_trace()
    name = await websocket.recv()
    global clients
    clients.add(websocket)
    for client in clients:
        await client.send("{} joined the conversation".format(name))
        while True:
            try:
                log_status = await websocket.recv()
                if log_status == "logging_on":
                    logging.getLogger(__name__).setLevel(logging.DEBUG)
                    logging.basicConfig(level=logging.DEBUG)
                elif log_status == "logging_off":
                    logging.getLogger(__name__).setLevel(logging.NOTSET)
                    logging.basicConfig(level=logging.NOTSET)
                new_message = "<b>DEBUG Log:</b> {}".format(log_status)
                for client in clients:
                    await client.send(new_message)
                    await client.send("*************************************")
                    await client.send("Monitoring Wirelss APs in JSON file")
                    await client.send("*************************************")
                    q = asyncio.Queue()
                    await q.put('no_modification')
                    msg = await q.get()
                    await client.send('\nDEBUG:\tCurrently ' + msg + ' in json file\n')
                    # A file which contains surrounding Wireless APs in JSON format
                    acc_points_file = 'C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json'
                    acc_points_path, filename = os.path.split(acc_points_file)
                    # A file which contains surrounding Wireless APs in JSON format before event triggered
                    access_points_before_event_file = 'C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_before_event.json'
                    # Copy json file before the event triggered
                    copyfile(acc_points_file, access_points_before_event_file)
                    await client.send("DEBUG:\tCopied json file before file modification\n")
                    await file_change_notification(client, acc_points_path, q)
                    await logger(client, q)
            except:
                clients.remove(websocket)


if __name__ == "__main__":
    clients = set()

    start_server = websockets.serve(monitor, '0.0.0.0', 5678)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

