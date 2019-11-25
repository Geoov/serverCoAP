
class Header():
    def __init__(self):
        self.header=""

        #version - 2-bit unsigned integer (CoAP version number )
        self.ver=""

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

        if self.tkl != 0 and (self.tkl > 0 and self.tkl <= 8):
            self.token = header[32:(32+8*self.tkl)]

        # if self.options != 0:
        #     self.options = header[128:160]
        # if self.payload != 0:
        #     self.payload = header[160:

# Setting and getting first 8 bits..

    def setVerTypeTkl(self, version, type, tkl):
        # self.ver = format(version,'02b')
        self.ver = version
        self.type = type
        self.tkl = tkl

    def getVersion(self):
        return format(self.ver,'02b');

    def getMessageType(self):
        return format(self.type,'02b');

    def getTokenLength(self):
        return format(self.tkl,'04b');

    # def getType(self):
    #     return int(self.type, 2);
    #
    # def getTokenLength(self):
    #     return int(self.tkl, 2);

# Setting and getting response code & class..

    def setResponseClassCode(self, responseClass, responseCode):
        self.respClass = responseClass
        self.respCode = responseCode

    def getResponseClass(self):
        return format(self.respClass,'03b');

    def getResponseCode(self):
        return format(self.respCode,'05b');

# Setting and getting message ID

    def setMessageID(self,messageID):
        self.messID = messageID

    def getMessageID(self):
        return format(self.messID,'016b');

# Setting and getting Token

    def setToken(self, token):
        if (int(self.getTokenLength(),2)) >0 and (int(self.getTokenLength(),2)) <=8:
            self.token = token
        else:
            print('Invalid value for token length...')

    def getToken(self):
        if self.token:
            return format(self.token, '0' + str(int(self.getTokenLength(),2) * 8) + 'b')

# Glue that damn functions

    def setHeader(self):
        if self.getTokenLength() > 0:
            self.header = str(self.getVersion()) + str(self.getMessageType()) + str(self.getTokenLength()) + str(self.getResponseClass()) + str(self.getResponseCode()) + str(self.getMessageID()) + str(self.getToken())
        else:
            self.header = str(self.getVersion()) + str(self.getMessageType()) + str(self.getTokenLength()) + str(self.getResponseClass()) + str(self.getResponseCode()) + str(self.getMessageID())

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
        print("Header= " + str(self.getHeader()))
        print("Header size= " + str(len(self.getHeader())))
