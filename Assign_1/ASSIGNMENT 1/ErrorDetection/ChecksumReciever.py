
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

def validate_checksum(data):
    calculated_checksum=calculate_checksum(data)
    return calculated_checksum == format(0,'016b')


def checkingChecksum(receivedData): 
    if(validate_checksum(receivedData)):
        print("NO ERROR\nACCCCCCCCEEEEPPPPTED!!\n\n")
    else:
        print("ERROR!!\nREJECTED!!\n\n")