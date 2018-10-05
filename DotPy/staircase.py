#!/bin/python3

import sys


n = int(input().strip())
i = 1
while (i <= n):
	j = 0
	while (j < (n - i)):
		print (" ", end='')
		j += 1
	k = 0
	while (k < i):
		print ("#", end='')
		k += 1
	if (i != 0):
		print ("")
	i += 1
