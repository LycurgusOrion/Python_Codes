def b2d(b):

    l = len(b) - 1
    num = 0
    for i in b:
        num += int(i) * (2**l)
        l -= 1
    
    return num


print(b2d(str(input())))