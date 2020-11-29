import timeit


def Sum():
    sum = 0
    for i in range(10001):
        sum = sum + i
    return sum


t1 = timeit.timeit(stmt=Sum, number=1)
print(t1)
