import socket
from Header import Header
from Package import Package

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('127.0.0.1',8085))

header=Header()
header.setVerTypeTkl(1, 0, 4)
header.setResponseClassCode(0,1)
header.setMessageID(31)
header.setToken(22)
header.setHeader()
# a = header.getResponseCode()
# print(a)

package = Package()
package.buildPackage(header.header, "temperatura")

s.sendto(package.getPackage(), ('127.0.0.1', 8085))


def afisareRaspuns(data,addr):
    # print(data)
    response_package = Package()
    response_package.pack = data
    (head, mess) = response_package.getPackageInfo()
    print(mess)

data,addr = s.recvfrom(1024)
if data:
    afisareRaspuns(data, addr)
# response_mesaj = response_package.getMessage()

# print(response_mesaj)

s.close()
