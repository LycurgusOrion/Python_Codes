#!/bin/python3

import sys

s = str(input().strip())
o = ""
i = 0
while (i < len(s)):
	if (s[i] == 'p'):
		o += "pair"
	elif (s[i] == 'i'):
		o += "int"
	i += 1

i = 0
cr = 0
ct = 0
while (i < len(o)):
	if (o[i] == 'r'):
		cr += 1
	elif (o[i] == 't'):
		ct += 1

i = 0
while (i < len (o)):
	if (cr % 2 == 0)


print (o)