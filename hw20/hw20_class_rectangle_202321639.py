from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def area(self):
        return self.h * self.w

    def perimeter(self):
        return 2 * (self.h + self.w)


rectangle = Rectangle(3, 4)
print(f"직사각형 넓이: {rectangle.area():.1f}, 둘레: {rectangle.perimeter()}")
