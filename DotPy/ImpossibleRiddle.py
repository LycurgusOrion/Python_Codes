
def Main():

	nums = [1, 3, 5, 7, 9, 11, 13, 15]
	len_nums = len(nums)

	magic_num = 30

	for i in range(len_nums):
		for j in range(len_nums):
			for k in range(len_nums):
				if ((nums[i] + nums[j] + nums[k]) == magic_num):
					print("{0} + {1} + {2} = {3}".format(nums[i], nums[j], nums[k], magic_num))


if __name__ == "__main__":
	Main()