import sys

def Main():

    args = list(map(int, sys.argv[1:]))
    x = args[0]

    temp = x
    sumd = 0

    while temp > 0:
        
        sumd += int(temp % 10)
        # print(sumd)
        temp = int(temp / 10)
        # print(temp)

    print (sumd)


if __name__ == "__main__":
    Main()