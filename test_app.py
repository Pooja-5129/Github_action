from app import add, divide
import pytest

def test_add():
    assert add(2, 6) == 8

def test_divide():
    assert divide(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)