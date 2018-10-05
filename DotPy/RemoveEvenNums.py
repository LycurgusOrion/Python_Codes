# Program to remove even numbers from a list
import sys


def Main():

    number_list = list(map(int, sys.argv[1:]))
    number_list = [element for element in number_list if element % 2 != 0]
    print(number_list)

if __name__ == "__main__":
    Main()


# OUTPUT
# C:\Users\Lycurgus Orion\Dropbox\Langs\Python>python RemoveEvenNums.py 44 12 13 4 7 1 5
# [13, 7, 1, 5]
