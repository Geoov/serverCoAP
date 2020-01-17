from Header import Header
from Package import Package

# from requestConnection import requestConnection
from apiConnection import apiConnection
# from apiConnectionReq import apiConnectionReq
import socket

# coding=utf-8
# -*- coding: utf-8 -*-


if __name__=="__main__":

    header=Header()
    header.setVerTypeTkl(1, 2, 4)
    header.setResponseClassCode(0,2)
    header.setMessageID(31)
    header.setToken(62)
    header.setHeader()

    header.Print()
    package = Package()
    package.buildPackage(header.header,"all")
    print("\n\n\n Package")
    a,b = package.getPackageInfo()

    # tok = header.getToken()
    print(a+""+b)
    # print(tok)

    # API = requestConnection()
    # API = apiConnection()
    # json = API.getWinningBets()

    # API = apiConnectionReq()
    # json = API.getAvioanie()
    # acii
    API = apiConnection()
    json, respCode = API.getWeatherInfo("Iasi","imperial")
    print(json)
    print(respCode)
