def isstr(str):
    if (ord(str)>=65 and ord(str)<=90)or (ord(str)>=97 and ord(str)<=122):
        return True
    else:
        return False
def func(str1):
    scount = 0
    ncount = 0
    ocount = 0
    for str in str1:
        if str.isdigit():
            ncount = ncount + 1
        elif isstr(str):
            scount = scount + 1
        else:
            ocount = ocount + 1
    print("数字有%d个,字母有%d个,其他字符有%d个"%(ncount,scount,ocount))

str = input()
func(str)