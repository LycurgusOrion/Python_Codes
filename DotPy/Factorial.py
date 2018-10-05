import sys
import time


def fact(n):
	if n <= 1:
		return 1
	else:
		return (n * fact(n - 1))


def Main():

	args = list(map(int, sys.argv[1:]))
	num = args[0]
	f = fact(num)
	print("Factorial of %d is %d " %(num, f))


if __name__ == "__main__":
	Main()
