def func(str1,str2):
    str = ''
    for i in str1:
        if i.lower() != str2.lower():
            str += i
    print("result: " + str)
str1 = input().strip()
str2 = input().strip()

func(str1,str2)