import math

x,y,z = input("请输入三个数：").split(' ')

x = eval(x)
y = eval(y)
z = eval(z)
result = (3*x+4*math.sqrt(x**2+2*y**2))/(1+math.cos(z**3))
print(result)