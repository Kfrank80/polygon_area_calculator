def shape_calculator():
    pass


class Rectangle:

    def __init__(self, initial_width, initial_height):
        self.width = initial_width
        self.height = initial_height
        pass

    def set_width(self, new_width):
        self.width = new_width
        pass

    def set_height(self, new_height):
        self.height = new_height
        pass

    def get_area(self):
        return self.width * self.height
        pass

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
        pass

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
        pass

    def get_picture(self) -> str:
        picture = str()
        if self.width <= 50 and self.height <= 50:
            for it in range(0, self.height):
                picture += f"{'*' * self.width}\n"
            pass
        else:
            picture = f"Too big for picture."
            pass
        return picture
        pass

    def get_amount_inside(self, other_shape):
        return self.width // other_shape.width * self.height // other_shape.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    pass


class Square(Rectangle):

    def __init__(self, initial_side):
        super().__init__(initial_side, initial_side)
        self.side = initial_side

    def set_side(self, new_side):
        self.width = self.height = self.side = new_side
        pass

    def set_width(self, new_side):
        self.width = self.height = self.side = new_side
        pass

    def set_height(self, new_side):
        self.width = self.height = self.side = new_side
        pass

    def __str__(self):
        return f"Square(side={self.side})"

    pass
