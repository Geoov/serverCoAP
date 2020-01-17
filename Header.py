
class Header():
    def __init__(self):
        self.header=""

        self.headerVerTypeTkl = ""

        #version - 2-bit unsigned integer (CoAP version number )
        self.ver=""

        code=""

        #type - 2-bit unsigned integer ( type of msg:
                                        # CON - 0
                                        # NCON - 1
                                        # ACK - 2
                                        # RST -3 )
        self.type=""

        #token length - 4-bit unsigned integer
        self.tkl=""

        #Response Class - 3-bit unsigned integer
        self.respClass=""

        #Response Code- 5-bit unsigned integer
        self.respCode=""

        #Message ID - 16-bit unsigned integer
        self.messID=""

        #token - 0/8 bytes
        self.token=""

        # #token - 0/8 bytes
        # self.options=""
        #
        # #token - 0/8 bytes
        # self.payload=""

    def headerAttributes(self, header):
        self.header = header

        self.ver = header[0:2]
        self.type = header[2:4]
        self.tkl = header[4:8]

        self.respClass = header[8:11]
        self.respCode = header[11:16]

        self.messID = header[16:32]

        # if self.tkl != 0 and (self.tkl > 0 and self.tkl <= 8):
        self.limit = 32+int(8*self.tkl)
        # print(self.limit)
        self.token = header[32:self.limit]
        # print(self.token)

        # if self.options != 0:
        #     self.options = header[128:160]
        # if self.payload != 0:
        #     self.payload = header[160:

# Setting and getting first 8 bits..

    def setVerTypeTkl(self, version, type, tkl):
        # self.ver = format(version,'02b')
        self.ver = format(version, '02b')
        self.type = format(type, '02b')
        self.tkl = format(tkl, '04b')
        # print(self.tkl)
        self.headerVerTypeTkl = (version<<6) + (type<<4) + tkl
        self.headerVerTypeTkl = format(self.headerVerTypeTkl, '08b')

    def setMessageType(self, type):
        # print(self.type)
        self.type = format(type, '02b')
        # print(self.type)

    def getVersion(self):
        return int(str(self.ver),2)

    def getMessageType(self):
        return int(str(self.type),2)

    def getTokenLength(self):
        return int(str(self.tkl),2)

    # def getType(self):
    #     return int(self.type, 2);
    #
    # def getTokenLength(self):
    #     return int(self.tkl, 2);

# Setting and getting response code & class..

    def setResponseClassCode(self, responseClass, responseCode):
        self.respClass = format(responseClass, '03b')
        self.respCode = format(responseCode, '05b')
        self.code = (responseClass << 5)+responseCode
        self.code = format(self.code, '08b')

    def getResponseClass(self):
        return int(str(self.respClass),2)

    def getResponseCode(self):
        return int(str(self.respCode),2)

# Setting and getting message ID

    def setMessageID(self,messageID):
        self.messID = format(messageID,'016b')

    def getMessageID(self):
        return int(str(self.messID),2)

# Setting and getting Token

    def setToken(self, token):
        if (self.getTokenLength() >0 and self.getTokenLength() <=8):
            self.token = format(token, '0'+str(self.getTokenLength()*8)+'b')
            # print(self.token)
        else:
            print('Invalid value for token length...')

    def getToken(self):
        if self.token:
            return int(str(self.token),2)

# Glue that damn functions

    def setHeader(self):
        if self.getTokenLength() > 0:
            self.header = str(self.ver) + str(self.type) + str(self.tkl) + str(self.respClass) + str(self.respCode) + str(self.messID) + str(self.token)
        else:
            self.header = str(self.ver) + str(self.type) + str(self.tkl) + str(self.respClass) + str(self.respCode) + str(self.messID)

    def getHeader(self):
        return self.header

    def Print(self):
        print("\n\nAttr-> ")
        print("CoAP Version= " + str(self.getVersion()))
        print("Message Type= " + str(self.getMessageType()))
        print("Token Length= "  + str(self.getTokenLength()))
        print("Response Class= " + str(self.getResponseClass()))
        print("Response Code= " + str(self.getResponseCode()))
        print("MessageId= " + str(self.getMessageID()))
        print("Token= " + str(self.getToken()))
        print("Header= " + str(self.header))
        print("Header size= " + str(len(self.getHeader())))
