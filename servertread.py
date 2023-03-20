from socket import *
import _thread as thread
import sys


def sip(conn, a):
    count = 0

    while True:
        mld = conn.recv(1000).decode()
        if (mld == "lolxd"):
            break
        count = count + 1
    count = count/1_000_000
    rate = count/30
    print("ID\tInterval\tReceived\tRate")
    print(a[0], ":", a[1], "\t0.0-30.0\t", int(count),
          "MB\t", "%.2f" % rate, "Mbps")
    conn.close()


serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 8081
server_ip = "127.0.0.1"

try:
    serverSocket.bind((server_ip, serverPort))
except:
    print("ERROR: Binding failed")
    sys.exit()

serverSocket.listen(10)

print("---------------------------------------------\nA simpleperf server is listening on port",
      serverPort, "\n---------------------------------------------")

while True:
    connectionSocket, addr = serverSocket.accept()
    print("A simpleperf client with <",
          addr[0], ":", addr[1], "> is connected with <", server_ip, ":", serverPort, ">")
    thread.start_new_thread(sip, (connectionSocket, addr))

serverSocket.close()
