### Wireless APs Websockets with browser user interface

#### Description:

Implemented front end html browser UI to enter name of the user, server address (IP address, Port number) to connect and option to select to enable/disable debug logging and for communicated with server using websockets 

I have implemented Wireless APs monitoring application and displays information in html page (browser(new UI)). Implemented using websockets and asynchronous programming.

##### Installed and used below python modules:

- For browser and server communication implemented using websockets 
- For Asynchronous programming using asyncio
- For Continuous monitoring of JSON using watchdog.observers - Observer
- for Event handling on specific file using watchdog.events - FileSystemEventHandler
- To copying files using shutil - copyfile
- For JSON file parsing using json
- To Compare Json files (dictionary files) using deepdiff - DeepDiff
- For text modification using re
- For enable/disable debug Log using logging

##### Implemented below files

- Json file - WirelessAP.json
- Python script - WirelessAPs_Monitor_Websockets_UI.py
- Html file - Wireless_APs_Monitor.html 
- temp.txt - generates for read/write during execution & removed once the task is completed

##### Open Command Prompt (cmd), run below commands to install modules

```
python -m pip install json
python -m pip install shutil
python -m pip install deepdiff
python -m pip install watchdog
python -m pip install websockets
python -m pip install asyncio
python -m pip install re
```

#### Execution - Scenario1:

##### Modify json file with same content like change in the order of content

##### Html file - Wireless_APs_Monitor.html

```
C:\Python37\MyScriptsSE\CodingExercise\AP\Wireless_APs_Monitor.html
```

##### Json file - WirelessAP.json

```
Open C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json
```

```
{
  "access_points": [
    {
      "ssid": "MyAP",
      "snr": 63,
      "channel": 11
    },
    {
      "ssid": "YourAP",
      "snr": 42,
      "channel": 1
    },
    {
      "ssid": "HisAP",
      "snr": 54,
      "channel": 6
    }
  ]
}
```

##### Modify WirelessAP.json file after few seconds with same content with order change

Here YourAP and HisAP locations are interchanged.  Even though the JSON file is modified the overall content is same.  

```
Open C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json
```

```
{
  "access_points": [
    {
      "ssid": "MyAP",
      "snr": 63,
      "channel": 11
    },
    {
      "ssid": "HisAP",
      "snr": 54,
      "channel": 6
    },
    {
      "ssid": "YourAP",
      "snr": 42,
      "channel": 1
    }
  ]
}
```

##### During execution generated 2 Json files for before and after event trigger (file modification) 

C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_before_event.json

C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_after_event.json

##### Run WirelessAPs_Monitor_Websockets.py in a terminal

```
C:\Python37\python.exe C:/Python37/MyScriptsSE/CodingExercise/AP/WirelessAPs_Monitor_Websockets_UI.py
```

##### Open up the Wireless_APs_Monitor.html page in browser 

```
Latha joined the conversation

Latha: Checking Wireless APs information

*************************************

Monitoring Wirelss APs in JSON file

*************************************

DEBUG:	Currently no_modification in json file

DEBUG:	Copied json file before file modification

DEBUG:	event_type	modified	in	src_path C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json

DEBUG:	Copied json file after file modification

DEBUG:	Wireless APs json file contents are same even after file changes
```



#### Execution - Scenario2: (with new UI)

##### Modify json file with changing contents like changing (ssid/snr/channel) values in json file

##### Html file - Wireless_APs_Monitor.html

```
C:\Python37\MyScriptsSE\CodingExercise\AP\Wireless_APs_Monitor.html
```

##### Json file - WirelessAP.json

```
Open C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json
```

```
{
  "access_points": [
    {
      "ssid": "MyAP",
      "snr": 63,
      "channel": 11
    },
    {
      "ssid": "YourAP",
      "snr": 42,
      "channel": 1
    },
    {
      "ssid": "HisAP",
      "snr": 54,
      "channel": 6
    }
  ]
}
```

#####  Modify WirelessAP.json file after few seconds with changing (ssid/snr/channel) values   

```
 Open C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json
```

```
{
  "access_points": [
    {
      "ssid": "MyAP",
      "snr": 82,
      "channel": 11
    },
    {
      "ssid": "YourAP",
      "snr": 42,
      "channel": 6
    },
    {
      "ssid": "HerAP",
      "snr": 71,
      "channel": 1
    }
  ]
}
```

##### During execution generated 3 Json files for before and after event trigger (file modification), temp.json

C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_before_event.json

C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_after_event.json

C:\Python37\MyScriptsSE\CodingExercise\AP\temp.json (file removed once the task is completed)

- ##### Run WirelessAPs_Monitor_Websockets.py in a terminal

```
C:\Python37\python.exe C:/Python37/MyScriptsSE/CodingExercise/AP/WirelessAPs_Monitor_Websockets_UI.py
```

##### Initial UI page

##### **[![Before entering details](https://github.com/LathaAr/CodingExercise/blob/master/AP/Images/1.png)

##### UI page with user input (logging enabled) and connected to server

##### ![After entering input with enable logging ](https://github.com/LathaAr/CodingExercise/blob/master/AP/Images/2.png)Console output for Enable Debug logging (logging_on)

```
C:\Python37\python.exe C:/Python37/MyScriptsSE/CodingExercise/AP/WirelessAPs_Monitor_Websockets_UI.py
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'<b>DEBUG Log:</b> logging_on', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'*************************************', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'Monitoring Wirelss APs in JSON file', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'*************************************', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'\nDEBUG:\tCurrently no_modification in json file\n', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'DEBUG:\tCopied json file before file modification\n', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'DEBUG:\tevent_type\tmodified\tin\tsrc_path\tC:\\Python37\\MyScriptsSE\\CodingExercise\\AP\\WAP\\WirelessAP.json', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'DEBUG:\tCopied json file after file modification\n', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'\nDEBUG:\tWireless APs json file contnents are not same', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'\nDEBUG:\tDisplay surrounding Wireless APs: ', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'\nINFO:\t"HisAP" is removed from the list', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'\nINFO:\t"HerAP" is added to the list with  SNR 71 and channel 1', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'\nINFO:\t"MyAP"\'s SNR has changed from 63 to 82', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'\nINFO:\t"YourAP"\'s channel has changed from 1 to 6', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server - state = CONNECTING
DEBUG:websockets.protocol:server - event = connection_made(<_SelectorSocketTransport fd=620 read=idle write=<idle, bufsize=0>>)
DEBUG:websockets.protocol:server - state = OPEN
```



##### UI page with user input (logging disabled)  and connected server

![After entering input with Disable Debug logging](https://github.com/LathaAr/CodingExercise/blob/master/AP/Images/4.png)

##### Console output for Disable Debug Logging (logging_off)

```
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'Latha joined the conversation', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server < Frame(fin=True, opcode=1, data=b'logging_off', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'<b>DEBUG Log:</b> logging_off', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'*************************************', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'Monitoring Wirelss APs in JSON file', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'*************************************', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'\nDEBUG:\tCurrently no_modification in json file\n', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'DEBUG:\tCopied json file before file modification\n', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'DEBUG:\tevent_type\tmodified\tin\tsrc_path\tC:\\Python37\\MyScriptsSE\\CodingExercise\\AP\\WAP\\WirelessAP.json', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'DEBUG:\tCopied json file after file modification\n', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'\nDEBUG:\tWireless APs json file contnents are not same', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'\nDEBUG:\tDisplay surrounding Wireless APs: ', rsv1=False, rsv2=False, rsv3=False)
DEBUG:websockets.protocol:server > Frame(fin=True, opcode=1, data=b'\nINFO:\t"HerAP"\'s channel has changed from 10 to 100', rsv1=False, rsv2=False, rsv3=False)
```

- ##### Browser output when the access info is changed in the json file

```
Latha joined the conversation

DEBUG Log: logging_on

*************************************

Monitoring Wirelss APs in JSON file

*************************************

DEBUG:	Currently no_modification in json file

DEBUG:	Copied json file before file modification

DEBUG:	event_type	modified	in	src_path C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json

DEBUG:	Copied json file after file modification

DEBUG:	Wireless APs json file contnents are not same

DEBUG:	Display surrounding Wireless APs:

INFO:	"HisAP" is removed from the list

INFO:	"HerAP" is added to the list with SNR 71 and channel 1

INFO:	"MyAP"'s SNR has changed from 63 to 82

INFO:	"YourAP"'s channel has changed from 1 to 6

Latha joined the conversation

DEBUG Log: logging_off

*************************************

Monitoring Wirelss APs in JSON file

*************************************

DEBUG:	Currently no_modification in json file

DEBUG:	Copied json file before file modification

DEBUG:	event_type	modified	in	src_path C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json

DEBUG:	Copied json file after file modification

DEBUG:	Wireless APs json file contnents are not same

DEBUG:	Display surrounding Wireless APs:

INFO:	"HerAP"'s channel has changed from 10 to 100

DEBUG Log: logging_off

*************************************

Monitoring Wirelss APs in JSON file

*************************************

DEBUG:	Currently no_modification in json file

DEBUG:	Copied json file before file modification
```

