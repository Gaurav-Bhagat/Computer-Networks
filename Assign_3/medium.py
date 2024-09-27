# medium.py
import socket
import time
import random
from threading import Thread
COLLISION_PROBABILITY = 0.1

class Medium:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def handle_sender(self, data, addr, sock):
            print(f"Medium in use by {addr}. Data: {data.decode()}")
            sock.sendto("ACK".encode(), addr)

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind((self.ip, self.port))
            print(f"Medium is ready at {self.ip}:{self.port}")

            while True:
                data, addr = sock.recvfrom(1024)
                Thread(target=self.handle_sender, args=(data, addr, sock)).start()

if __name__ == "__main__":
    medium_ip = "127.0.0.1"
    medium_port = 12345

    medium = Medium(medium_ip, medium_port)   #common medium..
    medium.run()
