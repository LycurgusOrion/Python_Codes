import sys


def Main():

    string_a = "Hello World!"
    string_b = list(string_a)
    tuple_a = (1, 2, 3, 4)
    tuple_b = list(tuple_a)

    print(string_a, tuple_a, sep="\n")

    string_b[2] = "00"
    string_a = "".join(string_b)
    tuple_b[2] = 10
    tuple_a = tuple(tuple_b)

    print(string_a, tuple_a, sep="\n")


if __name__ == "__main__":
    Main()
