s = "Hello World"
x = eval(input())
if x == 0:
    print(s)
elif x > 0:
    for i in {0,2,4,6,8,10}:
        print(s[i:i+2:1])
else :
    for i in range(len(s)):
        print(s[i:i+1:1])