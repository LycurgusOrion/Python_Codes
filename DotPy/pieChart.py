#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

i = 0
while (i < len(a)):
	sum = 0
	j = 0
	while (j < len(a[i])):
		sum += a[i][j]
		j += 1
	j = 0
	while (j < len(a[i])):
		print (int((a[i][j] / sum) * 360), end=" ")
		j += 1
	print("")
	i += 1