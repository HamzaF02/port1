from socket import *
import _thread as thread
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000
server_ip = "127.0.0.1"

try:
    serverSocket.bind((server_ip, serverPort))
except:
    print("ERROR: Binding failed")
    sys.exit()

serverSocket.listen(1)

print("---------------------------------------------\nA simpleperf server is listening on port XXXX\n---------------------------------------------")

connectionSocket, addr = serverSocket.accept()

print('Connected to', addr)
# thread.start_new_thread(clienting, (connectionSocket, addr))

count = 0

while True:

    mld = connectionSocket.recv(1000).decode()
    if (mld == "lolxd"):
        break
    count = count + 1

print(count)
serverSocket.close()
