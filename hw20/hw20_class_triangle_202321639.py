from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Triangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return (self.w * self.h) / 2

    def perimeter(self):
        return self.w + self.h + math.sqrt(self.w ** 2 + self.h ** 2)


triangle = Triangle(3, 4)
print(f"(직각)삼각형 넓이: {triangle.area()}, 둘레: {triangle.perimeter()}")
