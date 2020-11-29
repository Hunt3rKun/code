
sum = 0

def fib(n):
    return 1 and n <= 2 or fib(n - 1) +fib(n - 2)

for i in range(1,16):
    sum = (fib(i) / fib(i+3)) + sum
print(sum)

