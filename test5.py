
number = eval(input("请输入一个四位数:\n"))

def Encode(number):
    list_number = []
    list_number.append(number % 10)         # 个位
    list_number.append(number // 10 % 10)   # 十位
    list_number.append(number // 100 % 10)  # 百位
    list_number.append(number // 1000)      # 千位
    str1 = ''
    for i in range(0,4):
        list_number[i] += 5
        list_number[i] %= 10
        str1 += str(list_number[i])
    print(str1)
Encode(number)