#10101001   00101010   10101001
from ErrorDetection.fileReader import readingR

def setWrapSum(sum):
    temp =sum
    if(sum > 0xFFFF):
        temp = temp & 0xF0000
        temp = temp>>16
        sum += temp
        sum = sum & 0x0FFFF
    return sum

def calculate_checksum(data):
    sum =0
    for i in range(0,len(data),16):
        byte = data[i:i+16]
        sum += int(byte,2)
    wrapsum = setWrapSum(sum)
    checksum = (~wrapsum & 0xFFFF)
    return format(checksum,'016b')

def startCheckSum():
    data = readingR()
    x = calculate_checksum(data)  #sender
    data +=x
    return data