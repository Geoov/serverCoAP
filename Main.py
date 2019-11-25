from Header import Header

if __name__=="__main__":

    header=Header()

    header.setVerTypeTkl(2, 2, 6)
    header.setResponseClassCode(4,4)
    header.setMessageID(31)
    header.setToken(542)
    header.setHeader()

    header.Print()
