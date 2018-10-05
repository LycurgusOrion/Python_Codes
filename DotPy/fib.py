import argparse as ag

class Fibonacci:

	def __init__(self, num):
		self.num = num
		self.result = list()
		self.fib()

	def fib(self):
		a, b = 0, 1
		for i in range(self.num):
			self.result.append(a)
			a, b = b, a+b

	@property
	def get_result(self):
		return self.result


def Main():
	parser = ag.ArgumentParser()
	parser.add_argument("num", help="The fibonacci number to find", type=int)
	parser.add_argument("-f", "--full-sequence", help="Display the full fibonacci sequence till num", action="store_true")

	args = parser.parse_args()

	result = Fibonacci(args.num).result

	if args.full_sequence:
		print(result)
	else:
		print(result[-1])


if __name__ == "__main__":
	Main()
