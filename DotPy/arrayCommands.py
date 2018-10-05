#!/bin/python3

import sys

def rightShift(l, y):
   if len(l) == 0:
      return l
   y = -y % len(l)

   return l[y:] + l[:y]

def leftShift(l, y):
   if len(l) == 0:
      return l
   y = y % len(l)

   return l[y:] + l[:y]

def displaySum(l, r, a):
	# sum = 0
	# if (l <= r):
	# 	i = l
	# 	while (i <= r):
	# 		sum += a[i]
	# 		i += 1
	# 	print (sum)
	print (sum(a[l:r+1]))

b = [int(arr_temp) for arr_temp in input().strip().split(' ')]

a = [int(arr_temp) for arr_temp in input().strip().split(' ')]

i = 0
while (i < b[1]):
	cn = [int(arr_temp) for arr_temp in input().strip().split(' ')]
	if (cn[0] == 1):
		a = rightShift(a, cn[1])
	elif (cn[0] == 2):
		a = leftShift(a, cn[1])
	elif (cn[0] == 3):
		displaySum(cn[1], cn[2], a)
	i += 1