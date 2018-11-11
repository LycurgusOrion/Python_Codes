n = int(input())
# print(n)

list_min = []

x = 0
while x < n:
    
    if x%2 is not 0:
        ab = input()
    
    num_roses = int(input())
    
    prices = input().split(" ")
    prices = list(map(int, prices))
    
    max_sum = int(input())
    
    min_i = 0
    min_j = 0
    min_diff = 0
    for i in prices:
        for j in prices:
            # print("i + j", i+j)
            if (i + j) <= max_sum:
                # print("i - j", i-j)
                if (i - j) >= 0 and (i - j) <= min_diff:
                    min_j = j
                    min_i = i
                    min_diff = i - j
                elif (j - i) >= 0 and (j - i) <= min_diff:
                    min_j = j
                    min_i = i
                    min_diff = j - i
    
    # print("i, j, mindiff", min_i, min_j, min_diff)
    tup = (min_i, min_j)
    list_min.append(tup)
    
    x += 1
    # print("x", x)

# print(list_min)
for i, j in list_min:
    print("Deepak should buy roses whose prices are {0} and {1}.".format(i, j))