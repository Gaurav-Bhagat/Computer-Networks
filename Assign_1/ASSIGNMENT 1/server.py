from socket import *
import socket
import sys
import ErrorDetection.CRCReciever as a
import ErrorDetection.ChecksumReciever as b

s = socket.socket(family = AF_INET , type=SOCK_STREAM)
s.bind(('127.0.0.1',12347))
s.listen(5)

while True:
    try:
        print("Server is waiting")
        clt,addr = s.accept()
        print("client connected from",addr)
        while True:
            try:
                choice = clt.recv(1024)
                if not choice:
                    break
                choice = int.from_bytes(choice, byteorder='big')
                if(choice == 1):
                    data = clt.recv(1024)
                    data = data.decode('utf-8')
                    data1 = "111001010101000111100000001111101111001111"
                    sum = a.checkingCRC(data1)
                else:
                    data = clt.recv(1024)
                    data = data.decode('utf-8')
                    #data1 = "100000111100000011111111111010000111110001010110"
                    sum = b.checkingChecksum(data)
            except socket.error as e:
                    print(f"Socket error: {e}")
                    break
            except Exception as e:
                    print(f"Unexpected error: {e}")
                    break
        clt.close()
        print("Connection closed.")
    except Exception as e:
        print(f"Failed to accept connection: {e}")

s.close()
print("Server shut down.")  # sever never shut downs....