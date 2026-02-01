class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return Rectangle(self.get_square() + other.get_square(), 1)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        return Rectangle(self.get_square() * n, 1)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


if __name__ == '__main__':
    r1 = Rectangle(2, 4)
    r2 = Rectangle(3, 6)
    print(r1.get_square())
    print(r2.get_square())

    r3 = r1 + r2
    print(r3.get_square())

    r4 = r1 * 4
    print(r4.get_square())

    print(Rectangle(3, 6) == Rectangle(2, 9))
