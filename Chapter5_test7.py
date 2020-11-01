for i in range(1, 100000):
    sum = 0
    for factor in range(1, i):
        if i % factor == 0:
            sum = sum + factor
    if i == sum:
        print(i)
