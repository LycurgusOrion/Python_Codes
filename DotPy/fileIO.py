import sys
import os


max_arg = 3
exitString = "exit"

if(len(sys.argv) != max_arg):
    print("error invalid arguments!")
    sys.exit()

fileName = sys.argv[1]
fileOp = sys.argv[2]


def createFile():
    fw = open(fileName, "w")
    print("\nWrite something to the file : ")
    inputStr = ""
    while(inputStr != exitString):
        inputStr = input()
        if (inputStr == exitString):
            break
        fw.write(inputStr + "\n")
    fw.close()


def readFile():
    try:
        fr = open(fileName, "r")

    except FileNotFoundError:
        print("error : file not found!")
        sys.exit()

    text = fr.read()
    print(text)
    fr.close()


def appendFile():
    fw = open(fileName, "a")
    print("\nWrite something more to the file : ")
    inputStr = ""
    while(inputStr != exitString):
        inputStr = input()
        if (inputStr == exitString):
            break
        fw.write(inputStr + "\n")
    fw.close()


if(fileOp == "r"):
    readFile()
elif(fileOp == "w"):
    createFile()
elif(fileOp == "a"):
    appendFile()
elif(fileOp == "d"):
    os.remove(fileName)
else:
    print("Invalid File mode!")
    sys.exit()
