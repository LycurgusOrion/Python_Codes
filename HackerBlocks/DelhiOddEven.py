def main():

    n = int(input())
    cn = []

    while n > 0:
        cn.append(int(input()))
        n -= 1

    for i in cn:
        sum_even = 0
        sum_odd = 0
        for t in get_digits(i):
            if t % 2 == 0:
                sum_even += t
            else:
                sum_odd += t
        
        if (sum_even % 4 == 0) or (sum_odd % 3 == 0):
            print("YES")
        else:
            print("NO")



def get_digits(i):

    digits = []
    while i:
        digit = i % 10
        digits.append(digit)
        i //= 10

    return digits


if __name__ == "__main__":
    main()
