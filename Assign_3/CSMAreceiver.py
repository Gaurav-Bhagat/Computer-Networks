# receiver.py
import socket
import threading

class Receiver:
    def __init__(self, receiver_id, listen_ip, listen_port):
        self.receiver_id = receiver_id
        self.listen_ip = listen_ip
        self.listen_port = listen_port

    def receive(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind((self.listen_ip, self.listen_port))
            print(f"{self.receiver_id} is ready to receive data on port {self.listen_port}.")

            while True:
                data, addr = sock.recvfrom(1024)
                print(f"{self.receiver_id} received data: {data.decode()} from {addr}")

                # sock.sendto("ACK".encode(), addr)

def receiver_thread(receiver_id, listen_ip, listen_port):
    receiver = Receiver(receiver_id, listen_ip, listen_port)
    receiver.receive()

if __name__ == "__main__":
    listen_ip = "127.0.0.1"

    threading.Thread(target=receiver_thread, args=("Receiver1", listen_ip, 12346)).start()
    threading.Thread(target=receiver_thread, args=("Receiver2", listen_ip, 12347)).start()
