from ErrorDetection.fileReader import readingR


def crc(data, divisor):  
    div_len = len(divisor)  
    temp = data[0: div_len]
    while div_len < len(data):
        if temp[0] == '1':
            temp = strXor(divisor, temp) + data[div_len]
        else:
            temp = strXor('0' * div_len, temp) + data[div_len]
        div_len += 1  

    if temp[0] == '1':
        temp = strXor(divisor, temp)
    else:
        temp = strXor('0' * div_len, temp)
    check = temp  
    return check


def strXor(a, b):
    result = ''  
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result 

def checkCRC():
    data = readingR()
    #divisor = "11101011"
    divisor = "11000110011"
    appended_data = data + '0' * (len(divisor) - 1)  
    checkcrc = crc(appended_data, divisor)  
    #print("Remainder is:", checkcrc)
    #print("Data to be sent to Receiver:",data + checkcrc)
    return (data + checkcrc)