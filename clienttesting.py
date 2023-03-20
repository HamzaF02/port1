from socket import *
import sys
import time


clientSocket = socket(AF_INET, SOCK_STREAM)


try:
    clientSocket.connect(('127.0.0.1', 8081))
except:
    print("Failed to connect")
    sys.exit()


msg = open("transfer").read().encode()

count = 0

print(sys.getsizeof(msg))
end = time.time() + 30

while time.time() < end:
    clientSocket.send(msg)

clientSocket.send("lolxd".encode())
clientSocket.close()
