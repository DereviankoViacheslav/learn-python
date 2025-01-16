
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def is_square(self):
        return self.width == self.height

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height


rectangle = Rectangle(5, 10)

print("Rectangle area is: ", rectangle.area())
print("Rectangle perimeter is: ", rectangle.perimeter())
print("Rectangle is square: ", rectangle.is_square())

rectangle.resize(6, 6)

print("Rectangle area is: ", rectangle.area())
print("Rectangle perimeter is: ", rectangle.perimeter())
print("Rectangle is square: ", rectangle.is_square())
