from adder import add_numbers, substract_numbers, multiply_numbers, divide_numbers
import pytest

def test_add_numbers():
    assert add_numbers(2, 3) == 5

def test_substract_numbers():
    assert substract_numbers(5, 3) == 2

def test_multiply_numbers():
    assert multiply_numbers(4, 3) == 12

def test_divide_numbers():
    assert divide_numbers(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide_numbers(5, 0)