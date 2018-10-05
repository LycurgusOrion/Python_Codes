#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

i = 0
pd = 0
sd = 0
while (i < len(a)):
	j = 0
	while j < len(a[i]):
		
		if (((i + j) == (len(a) - 1))):
			sd += a[i][j]
			# print ("SD = ", sd, i, j)
		if (i == j):
			pd += a[i][j]
			# print ("PD = ", pd, i, j)
		j += 1
	i += 1

# sd += a[len(a)//2][len(a)//2]
diff = pd - sd
if (diff < 0):
	diff = - diff

# print ("\n| ", pd, " - ", sd, " | = ", diff)
print (diff)
