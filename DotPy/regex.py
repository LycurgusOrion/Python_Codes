import re
import argparse as ag


def Main():
	parser = ag.ArgumentParser()
	parser.add_argument("expression", help="The RegEx Expression")
	parser.add_argument("file_name", help="File to search the expression for")
	args = parser.parse_args()

	exp = re.compile(args.expression, re.M | re.I)

	search_file = open(args.file_name)
	line_num = 0

	for line in search_file.readlines():
		line = line.strip('\n\r')
		line_num += 1
		search_result = re.search(exp, line)
		if search_result:
			print(str(line_num), ": ", line)	


if __name__ == "__main__":
	Main()
