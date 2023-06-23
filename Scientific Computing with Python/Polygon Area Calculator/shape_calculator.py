class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for i in range(self.height):
            picture += "*" * self.width + "\n"
        print(picture)
        return picture

    def get_amount_inside(self, rect):
        num1 = self.width // rect.width
        num2 = self.height // rect.height
        result = num1 * num2
        return result


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

    def __repr__(self):
        return "Square(side=" + str(self.width) + ")"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        Square.set_side(self, side)

    def set_height(self, side):
        Square.set_side(self, side)
