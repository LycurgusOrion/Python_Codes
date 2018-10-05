#!/bin/python3

import sys

def timeConversion(s):
    if ("PM" in s):
    	x = int(s[:2])
    	if (x != 12):
    		x += 12
    	s = s.replace(s[:2], str(x))
    if ("AM" in s):
    	x = int(s[:2])
    	if (x == 12):
    		x = 0
    	s = s.replace(s[:2], '0' + str(x))
    s = s.replace(s[-2:], "")
    return s

s = input().strip()
result = timeConversion(s)
print(result)
