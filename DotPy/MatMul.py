import sys
import time


def Main():

	n = 2

	a = [[5, 5], [5, 5]]
	b = [[5, 5], [5, 5]]
	c = a[:]

	for i in range(n):
		for j in range(n):
			for k in range(n):
				c[i][j] += a[i][k] * b[k][j]
	
	print(c)


if __name__ == "__main__":
	start_time = time.perf_counter()
	Main()
	print("Execution Time = %ss" %(time.perf_counter() - start_time))
