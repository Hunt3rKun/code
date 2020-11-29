
def isWs(n):
    sum = 0
    for factor in range(1, n):
        if n % factor == 0:
            sum = sum + factor
    if n == sum:
        return True
    else:
        return False
print(isWs(6))