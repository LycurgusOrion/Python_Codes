#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
i = 0
min = 2**64 - 1
max = arr[0]
while (i < len(arr)):
	j = 0
	sum = 0
	while (j < len(arr)):
		if (j != i):
			sum += arr[j]
		j += 1
	# print (sum)
	if (max < sum):
		max = sum
	if (min > sum):
		min = sum
	i += 1

print (min, max)