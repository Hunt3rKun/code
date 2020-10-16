day = {1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:30}

def Leap_year(year):
    if year %4 ==0 and year %100 !=0:
        return True
    elif year%400 == 0:
        return True
year = eval(input("请输入年份：\n"))
month = eval(input("请输入月份：\n"))
if Leap_year(year):
    if month in day:
        print(day[month])
    else:
        print(29)
else:
    if month in day:
        print(day[month])
    else:
        print(28)