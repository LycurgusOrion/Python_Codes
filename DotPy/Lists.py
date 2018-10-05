# Trying lists in python

print("Enter size of List : ")
size = int(input())

lists = []

print("Enter random numbers : ")
for i in range(0, size):
    lists.append(int(input()))

print("\nThis is the list you entered :", lists)
