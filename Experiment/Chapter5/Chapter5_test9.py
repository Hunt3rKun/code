import math


def deco_rec(func):
    def check_call_func(a,b):
        if a>0 and b >0:
            return func(a,b)
        else:
            return "参数不合法"
    return check_call_func
def deco_cir(func):
    def check_call_func(r):
        if r>0 :
            return func(r)
        else:
            return "参数不合法"
    return check_call_func
def deco_tri(func):
    def check_call_func(a,b,c):
        if a>0 and b >0 and c>0:
            return func(a,b,c)
        else:
            return "参数不合法"
    return check_call_func
@deco_tri
def perimeter_Triangle(a,b,c):
    return (a+b+c)
@deco_cir
def perimeter_Circle(r):
    return (math.pi*r*2)
@deco_rec
def perimeter_Rectangle(a,b):
    return 2*(a+b)
print(perimeter_Rectangle(1,-2))
print(perimeter_Triangle(5,6,7))
print(perimeter_Circle(4))