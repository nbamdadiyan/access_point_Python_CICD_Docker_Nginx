FROM python:3.7.4 as app
RUN apt update -y && apt install -y nginx
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirment.txt
CMD [ "python3 ./AP/WirelessAPs_Monitor_Websockets_UI.py"]
FROM nginx:latest as nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf
