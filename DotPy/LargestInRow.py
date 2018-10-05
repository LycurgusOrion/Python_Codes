import sys
import time


def Main():

	args = list(map(int, sys.argv[1:]))
	
	row = args[0]
	col = args[1]

	a = [[]*col for i in range(row)]

	for i in range(row):
		for j in range(col):
			a[i].append(int(input("Enter the element [{0}][{1}]: ".format(i, j))))

	print(a)

	sum_row = []
	sum_col = []

	# Largest in each row
	for i in range(row):
		print("Maximum in row {0} = {1}".format(i, max(a[i])))
		sum_row.append(sum(a[i]))

	# Largest in each column
	maxi = a[0][0]
	for i in range(col):
		col_list = []
		for j in range(row):
			col_list.append(a[j][i])        
		print("Maximum in col {0} = {1}".format(i, max(col_list)))
		sum_col.append(sum(col_list))

	print(sum_col, sum_row)

	# Magic Square
	if sum_col == sum_row:
		print("Magic Square!")
	else:
		print("Not a Magic Square!")

	# Transpose
	transpose = [ list(i) for i in zip(*a)]
	print(transpose)

	# Sum
	sum_array = [[]*row for i in range(col)]
	for i in range(row):
		for j in range(col):
			sum_array.append(a[i][j] + transpose[i][j])
	print("Sum = {}".format(sum_array))

	# Difference
	diff_array = [[]*row for i in range(col)]
	for i in range(row):
		for j in range(col):
			diff_array.append(a[i][j] - transpose[i][j])
	print("Difference = {}".format(diff_array))

	# Multiplication
	mul = a[:]
	for i in range(row):
		for j in range(col):
			for k in range(row):
				mul[i][j] += a[i][k] * transpose[k][j]
	print("Multiplication = {}".format(mul))

	# Diagonal Sum
	d_sum = 0
	for i in range(row):
		for j in range(col):
			if i == j:
				d_sum += a[i][j]
	print("Trace = {0}".format(d_sum))

	# Norm
	squaresum = 0
	for i in range(row):
		for j in range(col):
			squaresum += a[i][j]**2
	norm_m = squaresum**0.5
	print("Norm of Matrix = {0}".format(norm_m))

	# Symmetry
	if mul == a:
		print("Symmetric Matrix")
	else:
		print("Non-Symmetric Matrix")


if __name__ == "__main__":
	Main()

# OUT{PUT}
# C:\Users\Lycurgus Orion\Dropbox\Langs\Python>python LargestInRow.py 3 3
# Enter the element [0][0]: 1
# Enter the element [0][1]: 2
# Enter the element [0][2]: 3
# Enter the element [1][0]: 4
# Enter the element [1][1]: 5
# Enter the element [1][2]: 6
# Enter the element [2][0]: 7
# Enter the element [2][1]: 8
# Enter the element [2][2]: 9
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Maximum in row 0 = 3
# Maximum in row 1 = 6
# Maximum in row 2 = 9
# Maximum in col 0 = 7
# Maximum in col 1 = 8
# Maximum in col 2 = 9
# [12, 15, 18] [6, 15, 24]
# Not a Magic Square!
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# Sum = [[], [], [], 2, 6, 10, 6, 10, 14, 10, 14, 18]
# Difference = [[], [], [], 0, -2, -4, 2, 0, -2, 4, 2, 0]
# Trace = 15
# Norm of Matrix = 16.881943016134134