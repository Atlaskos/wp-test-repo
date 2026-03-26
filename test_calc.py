from calc import multiply, divide

def test_multiply():
    assert multiply(3, 4) == 12

def test_multiply_zero():
    assert multiply(5, 0) == 0

def test_divide():
    assert divide(10, 2) == 5.0
