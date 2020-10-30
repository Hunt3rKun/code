def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def sumfib(num):
    sum = 0
    for i in range(1,num+1):
        sum += fib(i)
    return sum

print(sumfib(10))