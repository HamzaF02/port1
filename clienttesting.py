from socket import *
import sys
import time


clientSocket = socket(AF_INET, SOCK_STREAM)


try:
    clientSocket.connect(('127.0.0.1', 12000))
except:
    print("Failed to connect")
    sys.exit()


msg = open("transfer")

count = 0

end = time.time() + 30

while time.time() < end:
    clientSocket.sendfile(msg)

clientSocket.send("lolxd".encode())
clientSocket.close()
