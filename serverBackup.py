import socket
from Package import Package
from Header import Header
from Package import Package
from apiConnection import apiConnection


# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

API = apiConnection()
OK = 200
NOT_FOUND = 404
locatie = {}
unitate_masura = {}

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

    print("\nAntetul pe care l-am primit de la client")
    print(head)
    print("\nMesajul pe care l-am primit de la client este" + mess)
    # print(mess)

    header.headerAttributes(head)
    print("\nDetalii Header")
    header.Print()

    if (header.getResponseClass() == 0):
        if (header.getResponseCode() == 0):
            request = OK
            message = ""
            # sooo de implementat ack non-ack
        elif (header.getResponseCode() == 1):
            if (mess.lower() in ["coordonate", "temperatura", "presiune", "umiditate", "vizibilitate", "vant", "informatii_generale", "all"]):
                data_api, response_code_data = API.getWeatherInfo(locatie[addr], unitate_masura[addr])
                if(response_code_data == "200"):

                    #Data de la API
                    # print("\nData all api")
                    # print(data_api)

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

                    if (mess.lower() == "coordonate"):
                        request = OK

                        # message = (data['coord']['lat'], data['coord']['lon'])

                        message = "" + "Coordonatele orasului " + locatie[addr] + " sunt " + str(data_api['coord']['lat']) + " " + str(data_api['coord']['lon']) + "."


                        #nu prea are sens daar.. ma rog ideea e ca luam token-ul de la client si il adaugam in header-ul nou
                        token = header.getToken()
                        print(token)
                        header_resp.setToken(token)
                        header_resp.setHeader()

                        print("\nHeaderul pentru impachetare este:")
                        header_resp.Print()

                        pack_resp = Package()
                        pack_resp.buildPackage(header_resp.header, message)
                        #
                        s.sendto(pack_resp.getPackage(), addr)

                        # header_resp.Print()
                        # print "a intrat"
                        # print data
                        # print data['coord']['lat']
                        # print data['coord']['lon']

                        # decoded_date = data.decode()
                        # print decoded_date
                        # print decoded_date['coord']
                        # message = data[]
                        # for item in data:
                        #     print('{}'.format(item["coordonate"]))
                        # print(message)

                    elif (mess.lower() == "umiditate"):
                        # print "a intrat"
                        request = OK
                        message = data["main"]["humidity"]
                        print message

                    elif (mess.lower() == "presiune"):
                        request = OK
                        message = data["main"]["pressure"]

                    elif (mess.lower() == "temperatura"):
                        request = OK
                        message = data["main"]["temp"]

                    elif (mess.lower() == "umiditate"):
                        request = OK
                        message = data["main"]["humidity"]

                    elif (mess.lower() == "vizibilitate"):
                        request = OK
                        message = data["visibility"]

                    elif (mess.lower() == "vant"):
                        request = OK
                        message = data["wind"]

                    elif (m.lower() == "informatii_generale"):
                        request = OK
                        message = data["weather"]["description"]

                    elif (m.lower() == "all"):
                        request = OK
                        message = data
                else:
                    request = ERROR
                    message = "Server Data could not be accessed or the Location is invalid" + str(response_code_data)
                    print("Error at getting API data")
            else:
                request = ERROR
                message = "Wrong access to resource"
                print("Received a wrong GET request")

        elif (header.getResponseCode() == 2):
            if(mess[:8].lower()=="locatie:"):
                m=mess[8:].lower()
                print("The new location is = "+ m + " for address "+ str(addr))
                locatie[addr] = m
                request = OK
                message = ""
            else:
                request = ERROR
                print("Received a wrong POST request from address "+ str(addr))
                message = "Wrong Location Request"

    else:
        print("This method doesn't exist")
        request = ERROR
        message = data


# UDP_IP = "192.168.1.215"
# UDP_PORT = 3000

UDP_IP = "127.0.0.1"
UDP_PORT = 8080

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # address from internet,for udp
s.bind((UDP_IP, UDP_PORT))
print("Waiting for connections")

package = Package()
header = Header()

while 1:
    data, addr = s.recvfrom(512)
    print(str(data))
    print(str(addr))
    if data:
        procesareDate(addr,data)


s.close()
