import math


def Solution(a, b, c):
    delta = b**2 - 4 * a * c
    if a != 0 and delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("x1={0},x2={1}".format(x1,x2))
    elif a != 0 and delta == 0:
        return -b / (2 * a)
    elif a != 0 and delta < 0:
        x1 = str(-b / (2 * a)) + "+" + str(math.sqrt(-delta) / (2 * a)) + "i"
        x2 = str(-b / (2 * a)) + "-" + str(math.sqrt(-delta) / (2 * a)) + "i"
        print("x1={0},x2={1}".format(x1,x2))
    elif a == 0 and b != 0:
        return -c / b
    else:
        return "no solution"

a = input()
b = input()
c = input()
Solution(float(a),float(b),float(c))