
numbers = []
for i in range(3):
    number = eval(input("请输入第{}个整数:\n".format(i+1)))
    numbers.append(number)
for i in range(len(numbers)):
    max_number = max(numbers)
    print("{} ".format(max_number), end="")
    numbers.remove(max_number)
