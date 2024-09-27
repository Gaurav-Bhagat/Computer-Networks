from socket import *
import socket
import sys
import ErrorDetection.CRCSender as a
import ErrorDetection.ChecksumSender as b
import random


def generateBit(len):
    return random.randint(0, len-1)

def generateTwoBits(len):
    a = random.randint(0, len//2)
    b = random.randint(len//2 + 1, len-1)
    if(a+1 == b):
        b = b + 1
    return {a,b}

def generateBurstError(data):
    n = len(data) -1
    st = random.randint(0,n//2)
    end = random.randint((n//2+1) ,n) 
    dataList = list(data)
    for i in range (st,end+1):
        dataList[i] = '0' if dataList[i] == '1' else '1'
    return dataList


def generateoddErrors(data):
    n = len(data)
    odd=[]
    for i in range (1,n):
        if(i%2 == 1):
            odd.append(i)
    oddlen = len(odd)
    i = random.randint(0,oddlen-1)
    ind = odd[i]
    dataList =list(data)
    uniqueBits = random.sample(range(n),ind)
    for i in uniqueBits:
        dataList[i] = '0' if dataList[i] == '1' else '1'
    print("odd error:",ind)
    return dataList


def noisyChannel(data):
    #choice = int(input("\nEnter 1 FOR single bit error:\n2 FOR double bit error:\n3 FOR Odd numbers of errors\n4 FOR Burst Error:"))
    choice = 3
    if(choice == 1):
        ind = generateBit(len(data))  # have choices to select the error type....
        dataList = list(data)
        dataList[ind] = '0' if  dataList[ind] == '1' else '1'

    elif(choice == 2):
        #ind1 , ind2 = generateTwoBits(len(data))
        ind1 = 4
        ind2 = 36
        dataList = list(data)
        dataList[ind1] = '0' if  dataList[ind1] == '1' else '1'

        dataList[ind2] = '0' if  dataList[ind2] == '1' else '1'

    elif(choice == 3):
        dataList = generateoddErrors(data)

    else:
        dataList = generateBurstError(data)

    data = ''.join(dataList)
    return data


c = socket.socket(family = AF_INET , type=SOCK_STREAM)
c.connect(('127.0.0.1',12347))

z='y'
i = 1
try:
    while z!='n':
        #choice = int(input("\nEnter 1 FOR CYCLIC REDUNDENCY CHECK:\n2 FOR CHECKSUM:\n"))
        choice = 1
        ch = choice.to_bytes(4, byteorder='big')
        c.send(ch)
        if(choice == 1):
            data = a.checkCRC()
            
            print("\nData to be transferred:",data)
            #fu = int(input("\nEnter 1 FOR Noisy Channel:\n 2 FOR Noiseless Channel:\n"))
            fu = 2
            if(fu == 1):
                data = noisyChannel(data)     #give choices to noisy or noiseless channels..
                print("\nData transferred due to the noisy channel:",data)
            
            else:
                print("\nNo error has enduced as the channel is Noiseless!!")
            c.send(data.encode('utf-8'))
        else:
            data = b.startCheckSum()
            
            print("Data to be transferred:",data)
            
            #fu = int(input("\nEnter 1 FOR Noisy Channel:\n 2 FOR Noiseless Channel:\n"))
            fu = 2
            if(fu == 1):
                data = noisyChannel(data)     #give choices to noisy or noiseless channels..
                print("\nData transferred due to the noisy channel:",data)
            
            else:
                print("\nNo error has enduced as the channel is Noiseless!!")
            c.send(data.encode('utf-8'))
        x = input("Want to send for data(y/n):")
        z = x.lower()   
except KeyboardInterrupt:
    print("Exit")
c.close()
