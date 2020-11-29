import abc
import math


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getArea(self):
        pass

    @abc.abstractmethod
    def getPerimeter(self):
        pass


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getArea(self):
        p = (self.a + self.b + self.c) / 2
        area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print("三角形的面积为:%d" % area)

    def getPerimeter(self):
        print("三角形的周长为:%d" % (self.a + self.b + self.c))


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getArea(self):
        print("长方形的面积为:%d" % (self.a * self.b))

    def getPerimeter(self):
        print("长方形的周长为:%d" % (2 * (self.a + self.b)))


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def getArea(self):
        print("圆的面积为:%f" % (self.r * self.r * math.pi))

    def getPerimeter(self):
        print("圆的周长为:%f" % (2 * math.pi * self.r))


t = Triangle(3, 4, 5)
t.getArea()
t.getPerimeter()
r = Rectangle(6, 7)
r.getArea()
r.getPerimeter()
c = Circle(5)
c.getArea()
c.getPerimeter()