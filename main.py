from shape_calculator import Rectangle
from shape_calculator import Square


def shape_calculator():
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
    rectang = Rectangle(51, 1)
    print(rectang.get_picture())
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    shape_calculator()
