import os

def readingR():  #receiver reading...
    directory = os.getcwd()
    subpackage = 'ErrorDetection'
    #filename =input("Enter the file name:")
    filename = "InputData.txt"
    filepath = os.path.join(directory,subpackage,filename)
    f=open(filepath,'r')
    data = f.read()
    f.close()
    return data
