import socket
from Package import Package
from Header import Header
from Package import Package
from apiConnection import apiConnection
import sys
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
from threading import Thread
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.uic import loadUi
import os
from random import randrange

row_number = 0
method_variable = '00'
token_variable = ''
request_variable = ''
data_buffer_server = []

class rc_p(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("uir.ui",self)
        self.setWindowTitle("SERVER CoAP")
        self.start_button.clicked.connect(self.start_button_function)
        self.stop_button.clicked.connect(self.stop_button_function)
        self.refresh_button.clicked.connect(self.refresh_button_function)
        self.data = []
        self.row_number = 0

    def start_button_function(self):
        # execfile("server_bbb.py")
        os.system("python server.py")
    def stop_button_function(self):
        os.system("pkill -f server.py")
        #server.exit_function()
    def refresh_button_function(self):
        self.data = server.get_data
        self.tableWidget.insertRow(row_number)
        column_number = 0
        for result in data:
            self.tableWidget.setItem(self.row_number, column_number, QtWidgets.QTableWidgetItem(str(result)))
            column_number += 1
        self.row_number += 1

# def exit_function():
#     sys.exit()

API = apiConnection()
OK = 200
locatie = {}
unitate_masura = {}
locatiee = {}
 # 0 - pt Celsius //// 1 - pt Fahrenheit //// 2 - Kelvin

def procesareDate(addr,data):
    # print(addr)
    request = 0
    message = ""

    if (locatie.get(addr) == None):
        locatie[addr] = "Iasi"
        unitate_masura[addr] = "metric"

    package.pack = data
    (head, mess) = package.getPackageInfo()
    # head.buildPackage()
    request_variable = mess
    print("\nAntetul pe care l-am primit de la client " + head)
    print("\nMesajul pe care l-am primit de la client este " + mess)
    # print(mess)

    header.headerAttributes(head)
    print("\nDetalii Header")
    header.Print()

    if (header.getResponseClass() == 0):
        if (header.getResponseCode() == 0):
            method_variable = '00'
            request = OK
            message = ""
            # sooo de implementat ack non-ack
        elif (header.getResponseCode() == 1):
            method_variable = '01'
            if (mess.lower() in ["coordonate", "temperatura", "presiune", "umiditate", "vizibilitate", "vant", "all"]):
                data_api, response_code_data = API.getWeatherInfo(locatie[addr], unitate_masura[addr])
                if(response_code_data == "200"):

                    #Data de la API
                    print("\nData all api")
                    print(data_api)

                    #pregatesc response header-ul - creez o noua instanta practic
                    header_resp = Header()

                    #header-ul este initializat cu cel furnizat de catre client
                    header_resp.headerAttributes(head)

                    #vedem tipul mesajului
                    mesajType = header_resp.getMessageType()
                    # print("\n\n\n")
                    # print(mesajType)

                    if(mesajType == 0):
                        #con -> setam ack
                        header_resp.setMessageType(2)
                    elif(mesajType == 1):
                        #non-con -> setam cod + clasa
                        header_resp.setResponseClassCode(2,5)

                    # a = header_resp.getMessageType()
                    # print(a)
                    # header_resp.Print()

                    #nu prea are sens daar.. ma rog ideea e ca luam token-ul de la client si il adaugam in header-ul nou
                    token = header.getToken()
                    token_variable = token
                    print(token)
                    header_resp.setToken(token)

                    if (mess.lower() == "coordonate"):
                        request = OK

                        # message = (data['coord']['lat'], data['coord']['lon'])

                        message = "" + "Coordonatele orasului " + locatie[addr] + " sunt " + str(data_api['coord']['lat']) + " latitudine" + " si " + str(data_api['coord']['lon']) + " longitudine."
                        print(message)

                        header_resp.setResponseClassCode(2,3)
                        header_resp.setHeader()

                        print("\nHeaderul pentru impachetare este:")
                        header_resp.Print()

                        pack_resp = Package()
                        pack_resp.buildPackage(header_resp.header, message)
                        #
                        print(header_resp.header)
                        s.sendto(pack_resp.getPackage(), addr)

                    elif (mess.lower() == "umiditate"):
                        # print "a intrat"
                        request = OK

                        message = "" + "Umiditatea in orasul " + locatie[addr] + " are valoarea " + str(data_api['main']['humidity']) + "%."

                        header_resp.setResponseClassCode(2,3)
                        header_resp.setHeader()

                        print("\nHeaderul pentru impachetare este:")
                        header_resp.Print()

                        pack_resp = Package()
                        pack_resp.buildPackage(header_resp.header, message)
                        #
                        print(header_resp.header)
                        s.sendto(pack_resp.getPackage(), addr)

                    elif (mess.lower() == "presiune"):
                        request = OK

                        message = "" + "Presiunea atmosferica a orasului " + locatie[addr] + " este " + str(data_api['main']['pressure']) + " hPa."

                        header_resp.setResponseClassCode(2,3)
                        header_resp.setHeader()

                        print("\nHeaderul pentru impachetare este:")
                        header_resp.Print()

                        pack_resp = Package()
                        pack_resp.buildPackage(header_resp.header, message)
                        #
                        print(header_resp.header)
                        s.sendto(pack_resp.getPackage(), addr)

                    elif (mess.lower() == "temperatura"):
                        request = OK

                        # 0 - Celsius // 1 - Fahrenheit // 2 - Kelvin

                        f = open("flagTemp.py","r")
                        flag_from_file = f.read()
                        print(flag_from_file)

                        # if (str(0) in flag_from_file):
                        #     print("\nsalutare lume")


                        if (str(0) in flag_from_file):
                            print("\nSetat pe mod Celsius..")

                            temperatura = data_api["main"]["temp"]
                            temperatura_maxima = data_api["main"]["temp_max"]
                            temperatura_minima = data_api["main"]["temp_min"]
                            temperatura_resimtita = data_api["main"]["feels_like"]
                            message = "" + "Temperatura in orasul " + locatie[addr] + " este " + str(temperatura) + " gr. Celsius.\n" + "Maxima este de " + str(temperatura_maxima) + " gr. Celsius iar minima de " + str(temperatura_minima) + " gr. Celsius.\n" + "In ceea ce priveste temperatura resimtita, aceasta este de " + str(temperatura_resimtita) + " gr. Celsius din cauza vantului care are o viteza de " + str(data_api["wind"]["speed"]) + " km/h."

                        else:
                            if (str(1) in flag_from_file):
                                print("\nSetat pe mod Fahrenheit..")

                                temperatura = (data_api["main"]["temp"] * 1.8) + 32
                                temperatura_maxima = (data_api["main"]["temp_max"] * 1.8) + 32
                                temperatura_minima = (data_api["main"]["temp_min"] * 1.8) + 32
                                temperatura_resimtita = (data_api["main"]["feels_like"] * 1.8) + 32
                                message = "" + "Temperatura in orasul " + locatie[addr] + " este " + str(temperatura) + " gr. Fahrenheit.\n" + "Maxima este de " + str(temperatura_maxima) + " gr. Fahrenheit iar minima de " + str(temperatura_minima) + " gr. Fahrenheit.\n" + "In ceea ce priveste temperatura resimtita, aceasta este de " + str(temperatura_resimtita) + " gr. Fahrenheit din cauza vantului care are o viteza de " + str(data_api["wind"]["speed"]) + " km/h."

                            else:
                                if (str(2) in flag_from_file):
                                    print("\nSetat pe mod Kelvin..")

                                    temperatura = (data_api["main"]["temp"] + 273.15)
                                    temperatura_maxima = (data_api["main"]["temp_max"] + 273.15)
                                    temperatura_minima = (data_api["main"]["temp_min"] + 273.15)
                                    temperatura_resimtita = (data_api["main"]["feels_like"] + 273.15)
                                    message = "" + "Temperatura in orasul " + locatie[addr] + " este " + str(temperatura) + " gr. Kelvin.\n" + "Maxima este de " + str(temperatura_maxima) + " gr. Kelvin iar minima de " + str(temperatura_minima) + " gr. Kelvin.\n" + "In ceea ce priveste temperatura resimtita, aceasta este de " + str(temperatura_resimtita) + " gr. Kelvin din cauza vantului care are o viteza de " + str(data_api["wind"]["speed"]) + " km/h."



                        # message = "" + "Temperatura in orasul " + locatie[addr] + " este " + str(data_api["main"]["temp"]) + " gr. Celsius.\n" + "Maxima este de " + str(data_api["main"]["temp_max"]) + " gr. Celsius iar minima de " + str(data_api["main"]["temp_min"]) + " gr. Celsius.\n" + "In ceea ce priveste temperatura resimtita, aceasta este de " + str(data_api["main"]["feels_like"]) + " gr. Celsius din cauza vantului care are o viteza de " + str(data_api["wind"]["speed"]) + " km/h."
                        # message = "" + "Temperatura in orasul " + locatie[addr] + " este " + str(temperatura) + " gr. Celsius.\n" + "Maxima este de " + str(temperatura_maxima) + " gr. Celsius iar minima de " + str(temperatura_minima) + " gr. Celsius.\n" + "In ceea ce priveste temperatura resimtita, aceasta este de " + str(temperatura_resimtita) + " gr. Celsius din cauza vantului care are o viteza de " + str(data_api["wind"]["speed"]) + " km/h."

                        header_resp.setResponseClassCode(2,3)
                        header_resp.setHeader()

                        print("\nHeaderul pentru impachetare este:")
                        header_resp.Print()

                        pack_resp = Package()
                        pack_resp.buildPackage(header_resp.header, message)
                        #
                        print(header_resp.header)
                        s.sendto(pack_resp.getPackage(), addr)

                    elif (mess.lower() == "vizibilitate"):
                        request = OK
                        message = "" + "Vizibilitatea orasului " + locatie[addr] + " este in valoare de " + str(data_api['visibility']) + "."
                        # if (str(data_api['weather']['description']) == 'fog'):
                        #     # message= message + str(message) + " De asemenea ceata este prezenta!"
                            # print("da")

                        print message
                        header_resp.setResponseClassCode(2,3)
                        header_resp.setHeader()

                        print("\nHeaderul pentru impachetare este:")
                        header_resp.Print()

                        pack_resp = Package()
                        pack_resp.buildPackage(header_resp.header, message)
                        #
                        print(header_resp.header)
                        s.sendto(pack_resp.getPackage(), addr)

                    elif (mess.lower() == "vant"):
                        request = OK
                        message = "" + "Vantul are o viteza de " + str(data_api["wind"]["speed"]) + " km/h batand cu un unghi de " + str(data_api["wind"]["deg"]) + " grade."

                        header_resp.setResponseClassCode(2,3)
                        header_resp.setHeader()

                        print("\nHeaderul pentru impachetare este:")
                        header_resp.Print()

                        pack_resp = Package()
                        pack_resp.buildPackage(header_resp.header, message)
                        #
                        print(header_resp.header)
                        s.sendto(pack_resp.getPackage(), addr)

                    elif (mess.lower() == "all"):
                        request = OK
                        message = data

                        message = "" + " Oras: " + locatie[addr] + "\n Temperatura: " + str(data_api["main"]["temp"]) + " gr. Celsius." + "\n Temperatura resimtita: " + str(data_api["main"]["feels_like"]) + " gr. Celsius." + "\n Temperatura maxima: " + str(data_api["main"]["temp_max"]) + " gr. Celsius." + "\n Temperatura minima: " + str(data_api["main"]["temp_min"]) + " gr. Celsius." + "\n Viteza vandului: " + str(data_api["wind"]["speed"]) + " km/h." + "\n Umiditatea: " + str(data_api['main']['humidity']) + "%." + "\n Presiunea atmosferica: " + str(data_api['main']['pressure']) + " hPa." + "\n Vizibilitatea: " + str(data_api['visibility']) + "."


                        header_resp.setResponseClassCode(2,3)
                        header_resp.setHeader()

                        print("\nHeaderul pentru impachetare este:")
                        header_resp.Print()

                        pack_resp = Package()
                        pack_resp.buildPackage(header_resp.header, message)
                        #
                        print(header_resp.header)
                        s.sendto(pack_resp.getPackage(), addr)
                else:

                    message = "Server Data could not be accessed or the Location is invalid. Cod eroare: " + str(response_code_data)
                    print("Error at getting API data")

                    pack_resp = Package()
                    pack_resp.buildPackage(header_resp.header, message)
                    #
                    s.sendto(pack_resp.getPackage(), addr)
            else:
                ERROR_CODE = 400
                message = "Received an invalid GET request."
                message = message + "\n" + str(ERROR_CODE) + " - Bad Request."


                header_resp = Header()
                header_resp.headerAttributes(head)

                header_resp.setResponseClassCode(4,0)
                header_resp.setHeader()

                pack_resp = Package()
                pack_resp.buildPackage(header_resp.header, message)
                #
                s.sendto(pack_resp.getPackage(), addr)

        elif (header.getResponseCode() == 2):
            method_variable = '10'
            if(mess[:8].lower()=="locatie:"):
                request = OK
                new_location=mess[8:].lower()
                locatiee = new_location
                locatie[addr] = new_location

                header_resp = Header()
                header_resp.headerAttributes(head)

                message = "The new location is set to " + new_location + ".. Have Fun :)"

                pack_resp = Package()
                pack_resp.buildPackage(header_resp.header, message)
                #
                s.sendto(pack_resp.getPackage(), addr)

            else:
                ERROR_CODE = 405
                message = "Wrong Location Request"
                message = message + "\n" + str(ERROR_CODE) + " - Method not allowed."

                pack_resp = Package()
                header_resp = Header()
                header_resp.headerAttributes(head)

                header_resp.setResponseClassCode(4,5)
                header_resp.setHeader()

                pack_resp = Package()
                pack_resp.buildPackage(header_resp.header, message)
                #
                s.sendto(pack_resp.getPackage(), addr)
        elif (header.getResponseCode() == 3):
            request = OK
            method_variable = '11'

            # if (flag_temperatura == 0):
            #     flag_temperatura = 1
            # else:
            #     if (flag_temperatura == 1):
            #         flag_temperatura = 0

            flag_temperatura = randrange(3)
            print(flag_temperatura)

            f = open("flagTemp.py", "w")
            # print(f.read())
            f.write("flag_temperatura = " + str(flag_temperatura))

            if (flag_temperatura == 0):
                message = "Temperatura setata pe mod Celsius"

                pack_resp = Package()
                header_resp = Header()
                header_resp.headerAttributes(head)

                header_resp.setResponseClassCode(2, 0)
                header_resp.setHeader()

                pack_resp = Package()

                pack_resp.buildPackage(header_resp.header, message)

                s.sendto(pack_resp.getPackage(), addr)


            else:
                if (flag_temperatura == 1):
                    message = "Temperatura setata pe mod Fahrenheit"

                    pack_resp = Package()
                    header_resp = Header()
                    header_resp.headerAttributes(head)

                    header_resp.setResponseClassCode(2, 0)
                    header_resp.setHeader()

                    pack_resp = Package()

                    pack_resp.buildPackage(header_resp.header, message)
                    s.sendto(pack_resp.getPackage(), addr)


                else:
                    if (flag_temperatura == 2):
                        message = "Temperatura setata pe mod Kelvin"

                        pack_resp = Package()
                        header_resp = Header()
                        header_resp.headerAttributes(head)

                        header_resp.setResponseClassCode(2, 0)
                        header_resp.setHeader()

                        pack_resp = Package()

                        pack_resp.buildPackage(header_resp.header, message)
                        s.sendto(pack_resp.getPackage(), addr)



    else:
        print("This method doesn't exist")
        method_variable = '20'
        request = 402
        message = data


# UDP_IP = "192.168.1.215"
# UDP_PORT = 3000

UDP_IP = "127.0.0.1"
UDP_PORT = 8085

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # address from internet,for udp
s.bind((UDP_IP, UDP_PORT))
print("Se asteapta conexiuni...")

package = Package()
header = Header()
# SW = 1
# def collector(collect_from):
while 1:
    data_buffer = []
    data, addr = s.recvfrom(1024)

    print(str(data))
    print(str(addr))
    if data:
        procesareDate(addr,data)
        data_buffer.append(addr)
        data_buffer.append(UDP_PORT)
        if method_variable == '00':
            data_buffer.append('EMPTY')
        else:
            if method_variable == '01':
                data_buffer.append('GET')
            else:
                if method_variable == '10':
                    data_buffer.append('POST')
                else:
                    if method_variable == '11':
                        data_buffer.append('CUSTOM')
                    else:
                        data_buffer.append('WRONG METHOD')

        data_buffer.append(token_variable)
        data_buffer.append(request_variable)
        data_buffer_server = data_buffer
        print(data_buffer_server)
#
# collector_thread = Thread(target = collector, args=)
# collector_thread.start()
#
app = QtWidgets.QApplication(sys.argv)
window = rc_p()
window.show()
app.exec_()




s.close()
