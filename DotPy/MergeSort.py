def mergeSort(array, l, r, m):
	
	a = m - l + 1
	b = r - m

	left_arr = []
	right_arr = []

	for i in range(int(a)):
		left_arr.append(array[int(l + i)])
	for j in range(int(b)):
		right_arr.append(array[int(m + 1 + j)])

	print(left_arr)
	print(right_arr)
	
	i = 0
	j = 0
	k = l

	while i < a and j < b:
		if left_arr[i] < right_arr:
			array[k] = left_arr[i]
			i+=1
		else:
			array[k] = right_arr[j]
			j+=1
		k += 1

	print(i, a, b, array)
	while i < a:
		array[k] = left_arr[i]
		i += 1
		k += 1
	
	while j < b:
		array[k] = right_arr[j]
		j += 1
		k += 1
	

def merge(array, l, r):
	if l == r:
		return 0
	if l < r:
		m = (l + (r - 1)) / 2
		merge(array, l, m)
		merge(array, m + 1, r)
		mergeSort(array, l, m, r)


def Main():
	array = [1, 32, 2, 45, 30, 12]
	print(array)
	merge(array, 0, len(array) - 1)
	print(array)


if __name__ == "__main__":
	Main()

