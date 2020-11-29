a, b, c = input("请输入长方体的三条边的长度：").split(' ')

def Volume(a,b,c):
    return a*b*c

def Superfical_area(a,b,c):
    return 2*(a*b+b*c+a*c)

print("体积：%lf"%Volume(eval(a),eval(b),eval(c)))
print("表面积：%lf"%Superfical_area(eval(a),eval(b),eval(c)))