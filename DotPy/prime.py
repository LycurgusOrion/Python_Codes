import time
import sys


def prime(x):
	i = 0
	for i in range(2, x):
		if x % i == 0:
			return 0
	if i == x:
		return 1


def Main():
	
	args = list(map(int, sys.argv[1:]))
	x = args[0]

	if prime(x) == 0:
		print("%d is not a prime number!" %(x))
	else:
		print("%d is a prime number!" %(x))


if __name__ == "__main__":
	Main()