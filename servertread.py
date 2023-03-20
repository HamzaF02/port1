from socket import *
import _thread as thread
import sys


def sip(conn):
    count = 0

    while True:
        mld = conn.recv(1000).decode()
        if (mld == "lolxd"):
            break
        count = count + 1

    print(count)
    conn.close()


serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000
server_ip = "127.0.0.1"

try:
    serverSocket.bind((server_ip, serverPort))
except:
    print("ERROR: Binding failed")
    sys.exit()

serverSocket.listen(10)

print("---------------------------------------------\nA simpleperf server is listening on port XXXX\n---------------------------------------------")

while True:
    connectionSocket, addr = serverSocket.accept()
    print("A simpleperf client with <", addr, ": ", addr,
          " > is connected with < 127.0.0.1 : 12000 >")
    thread.start_new_thread(sip, (connectionSocket, addr))

serverSocket.close()
