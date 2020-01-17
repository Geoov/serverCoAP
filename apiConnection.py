# coding=utf-8
# -*- coding: utf-8 -*-
import socket
import json
import re
# import json as simplejson

class apiConnection():
    def __init__(self):
        pass

    def getWeatherInfo(self, locatie, unitate_masura):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            socket.setdefaulttimeout(1)
            # s.connect(('api.nasa.gov', 443))
            s.connect(("api.openweathermap.org", 80))
        except socket.error as ex:
            print(ex)
            print("error 1...")
            print("\n")
            con_error = "error 2..."

        # request = 'GET /lol/champions?token=p6EkCqdt1pVf0FaiSW7cls6fIfUyJDcz_RIhAwPoYq57Pc9ijqg HTTP/1.1\r\nHost: api.pandascore.co\r\n\r\n'
        # s.sendall(request.encode('utf-8'))

        # s.sendall("GET /lol/champions?token=p6EkCqdt1pVf0FaiSW7cls6fIfUyJDcz_RIhAwPoYq57Pc9ijqg HTTP/1.1\r\nHost: api.pandascore.co\r\n\r\n")

        # s.sendall('GET /planetary/apod?api_key=CJdQV1LWyWDGQRFPcZ9KCWitdgmGpxlOAOLHCj5A HTTPS/1.1\r\nHost: api.nasa.gov\r\n\r\n')
        # s.sendall('GET api.nasa.gov/planetary/apod?api_key=CJdQV1LWyWDGQRFPcZ9KCWitdgmGpxlOAOLHCj5A');

        request = "GET /data/2.5/weather?q="+locatie+"&APPID=067082138e4d3856bd8ca01b9cc63c87&units="+unitate_masura+" HTTP/1.1\r\nHost: api.openweathermap.org\r\n\r\n"
        s.send(request.encode())
        response = s.recv(1024)
        response = response.decode('utf-8')

        response_code=re.findall(r"([0-9]{3})",response)[0]
        y = response.rfind('\n')
        jsonData=json.loads(response[y + 1:])
        # print(response[y+1:])
        return jsonData, response_code
