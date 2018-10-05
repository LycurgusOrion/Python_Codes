print("Python sucks")

x = int(input("Enter any number : "))

print(x)

for i in range(2, int(x / 2)):
	if (x % i) == 0:
		print("Nope, not a prime number!")
		break
	else:
		print(i)

# print(i, int(x / 2))

if i == int(x / 2) - 1:
	print("It's a prime numero!")
