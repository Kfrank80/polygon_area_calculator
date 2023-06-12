from shape_calculator import Rectangle
from shape_calculator import Square


class TestRectangle:

    def test_1(self):
        assert 1 == 1
        pass

    def test_init(self):
        rect = Rectangle(20, 12.6)
        assert isinstance(rect, Rectangle)
        assert rect.width == 20
        assert rect.height == 12.6
        pass

    def test_set_width(self):
        rect = Rectangle(20, 30)
        rect.set_width(2.46)
        assert rect.width == 2.46
        pass

    def test_set_height(self):
        rect = Rectangle(2.74, 5.79)
        rect.set_height(6.54)
        assert rect.height == 6.54
        pass

    def test_get_area(self):
        rect = Rectangle(5, 5)
        assert rect.get_area() == 25
        pass

    def test_get_perimeter(self):
        rect = Rectangle(5, 5)
        assert rect.get_perimeter() == 20
        pass

    def test_get_diagonal(self):
        rect = Rectangle(5.23, 5)
        assert rect.get_diagonal() == (rect.width ** 2 + rect.height ** 2) ** .5
        pass

    def test_get_picture(self):
        # Included in main
        pass

    def test_get_amount_inside(self):
        rect = Rectangle(1, 0.5)
        rect1 = Rectangle(1, 1)
        assert rect1.get_amount_inside(rect) == 2
        pass

    pass


class TestSquare:

    def test_1(self):
        assert 1 == 1
        pass

    def test_set_side(self):
        sq = Square(4.3)
        assert sq.side == sq.width and sq.side == sq.height
        sq.set_side(4.12)
        assert sq.side == 4.12
        pass

    def test_set_width(self):
        sq = Square(5.67)
        sq.set_width(6.78)
        assert sq.width == 6.78
        pass

    def test_set_height(self):
        sq = Square(87.45)
        sq.set_height(5.15)
        assert sq.height == 5.15
        pass

    pass
