#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    i = 0
    max = ar[0]
    while (i < n):
    	if (max < ar[i]):
    		max = ar[i]
    	i += 1
    c = 0
    i = 0
    while (i < n):
    	if (ar[i] == max):
    		c += 1
    	i += 1
    return c

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
