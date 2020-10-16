
rows = 4
row = 1
while row <= rows:
    col = 1
    while col <= (rows -row):
        print('    ', end='')
        col += 1
    print((2*row-1) * '*   ')
    row += 1

bottom = rows -1
while bottom > 0:
    col = 1
    while bottom +col <= rows:
        print('    ', end='')
        col += 1
    print((2*bottom-1) * '*   ')
    bottom -= 1