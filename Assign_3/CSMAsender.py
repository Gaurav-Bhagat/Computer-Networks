# sender   ---->   medium    ---->   receiver
import random
import socket
import time
import threading

sending =[False,False]

list0 = [1000,1001,1100,1111,0000]
list1 = [1000,1001,1100,1111,0000]

comp = [False,False]
mutex = threading.Lock()

class Sender:
    def __init__(self, sender_id, p, medium_ip, medium_port):
        self.sender_id = sender_id
        self.p = p
        self.medium_ip = medium_ip
        self.medium_port = medium_port
        self.k = 0

    def send(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            while True:
                R = random.random()
                if R < self.p:
                    sending[self.sender_id] =True
                    print(f"{self.sender_id} attempting to send data...")
                    sock.sendto(f"{self.sender_id}: {list0[self.k]}".encode(), (self.medium_ip, self.medium_port))
                    time.sleep(random.uniform(0.1, 0.3))  #propagation time
                    
                    while sending[0] == True and sending[1] == True:
                            print(f"{self.sender_id}: Collsion.....have to resend the data{list0[self.k]} again..")
                            self.col()
                    else:
                        sending[self.sender_id] =False
                        print(f"\nSender {self.sender_id} is SUCCESSFULLY send the data{list0[self.k]}\n")
                        
                        self.k = self.k + 1
                        response, _ = sock.recvfrom(1024)
                        response = response.decode()
                    
                else:
                    print(f"{self.sender_id}: p < R ----> Waiting to retry...")
                    time.sleep(random.uniform(1, 5))
                
                if(self.k == 4):
                    comp[self.sender_id] =True
                    sending[self.sender_id] =False
                    while(comp[0] != True or comp[1] != True):
                        pass
                    break
    def col(self):
        mutex.acquire()
        try:
            time.sleep(random.uniform(1, 2))  #backoff
            sending[self.sender_id] = False
        finally:
            mutex.release()

def sender_thread(sender_id, p, medium_ip, medium_port):
    sender = Sender(sender_id, p, medium_ip, medium_port)
    sender.send("Hello")

if __name__ == "__main__":
    medium_ip = "127.0.0.1"
    medium_port = 12345

    t0 = threading.Thread(target=sender_thread, args=(0, 0.5, medium_ip, medium_port))
    t1 = threading.Thread(target=sender_thread, args=(1, 0.5, medium_ip, medium_port))
    
    t0.start()  # Sender - 0
    t1.start()  # Sender - 1

    t0.join()
    t1.join()
    
    print("All sent!!")
