import sys
x = float(sys.argv[1])
precision = 10
for i in range(precision):
	x *= 2
	y = int(x)
	print(y, x)
	x -= y