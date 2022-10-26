from src.Square import Square

def get_area():
    square = Square(2)
    assert Square.area == 9
    print(square.area)

def test_perimeter():
    square = Square(4)
    assert Square.perimeter == 12