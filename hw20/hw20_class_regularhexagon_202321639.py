from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class RegularHexagon(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return (3 * math.sqrt(3) * self.s ** 2) / 2

    def perimeter(self):
        return 6 * self.s


regular_hexagon = RegularHexagon(4)
print(f"정육각형 넓이: {regular_hexagon.area():.1f}, 둘레: {regular_hexagon.perimeter()}")