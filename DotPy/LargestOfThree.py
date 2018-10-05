import sys


def Main():

	args = sys.argv[1:]
	args = list(map(int, args))
	maxi = args[0]

	for i in range(len(args)):
		if args[i] > maxi:
			maxi = args[i]
	
	print(maxi, end="")


if __name__ == "__main__":
	Main()
	