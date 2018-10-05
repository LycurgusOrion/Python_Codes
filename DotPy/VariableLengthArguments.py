def sum(*args):

    total = 0
    for i in args:
        total += i
    return total


print(sum(123, 456, 789))
