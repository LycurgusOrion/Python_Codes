#!/bin/python3

import sys

def updateValue(a, i, x):
	j = 0
	while (j < len(a)):
		if (j == i):
			a[j] = x
		j += 1

def displayOutput(a, i):
	

input_n_q = [int(arr_temp) for arr_temp in input().strip().split(' ')]

a = [int(arr_temp) for arr_temp in input().strip().split(' ')]

i = 0
while (i < input_n_q[1]):
	cn = [int(arr_temp) for arr_temp in input().strip().split(' ')]
	if (cn[0] == 1):
		a = updateValue(a, cn[1], cn[2])
	elif (cn[0] == 2):
		displayOutput(a, i)
	i += 1