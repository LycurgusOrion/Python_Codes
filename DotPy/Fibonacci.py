

def Main():

	a = 0
	b = 1
	n = int(input("Enter n..."))

	s = [0, 1]

	for i in range(n):
		c = a + b
		s.append(c)
		a = b
		b = c
	
	print(s)


if __name__ == "__main__":
	start_time = time.time()
	Main()
	print("Executed in %ss" %(time.time() - start_time))