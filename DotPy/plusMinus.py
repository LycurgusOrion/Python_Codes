#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

i = 0
neg = 0
pos = 0
zer = 0
while (i < len(arr)):
	if (arr[i] > 0):
		pos += 1
	if (arr[i] == 0):
		zer += 1
	if (arr[i] < 0):
		neg += 1
	i += 1

pos = pos / len(arr)
neg = neg / len(arr)
zer = zer / len(arr)

print (pos)
print (neg)
print (zer)