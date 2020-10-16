#简单图形绘制
import turtle as t
import math
def main():
    t.pensize(14)
    t.pu()
    t.goto(-150,50)
    t.pd()
    t.seth(72)
    t.begin_fill()
    t.color("yellow")
    t.circle(-150 / math.cos(18 * math.pi / 180)-10)
    t.end_fill()
    t.seth(-18)
    t.fd(10)
    t.seth(72)
    t.begin_fill()
    t.color("blue")
    t.circle(-150 / math.cos(18 * math.pi / 180))
    t.end_fill()
    t.seth(0)
    t.begin_fill()
    t.color("red")
    for i in range(5):
        t.fd(300)
        t.rt(144)
    t.end_fill()
    t.exitonclick()
if __name__ == '__main__':
    main()

