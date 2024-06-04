from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r


class Rectangle(Shape):
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def area(self):
        return self.h * self.w

    def perimeter(self):
        return 2 * (self.h + self.w)


class RegularHexagon(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return (3 * math.sqrt(3) * self.s ** 2) / 2

    def perimeter(self):
        return 6 * self.s


class Triangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return (self.w * self.h) / 2

    def perimeter(self):
        return self.w + self.h + math.sqrt(self.w ** 2 + self.h ** 2)


def main():
    shapes = []
    shapes.append(Circle(5))
    shapes.append(Rectangle(5, 3))
    shapes.append(RegularHexagon(5))
    shapes.append(Triangle(5, 3))

    for shape in shapes:
        print(f"{type(shape).__name__}의 넓이는 {shape.area():.1f}")
        print(f"{type(shape).__name__}의 둘레는 {shape.perimeter():.1f}")

if __name__ == "__main__":
    main()
