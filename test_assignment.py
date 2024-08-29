import pytest
import  assignment

def test_hello():
    assert assignment.hello_world() == "Hello World!"


@pytest.mark.parametrize("input, expected", [(1, 3), (10, 12), (-4, -2)])
def test_add_two(input, expected):
    assert assignment.add_two(input) == expected

def test_convert_to_lowercase():
    assert assignment.convert_to_lowercase("HELLO") == "hello"

def test_convert_to_uppercase():    
    assert assignment.convert_to_uppercase("hello") == "HELLO"

def test_convert_to_titlecase():
    assert assignment.convert_to_titlecase("hello") == "Hello"

def test_add_exclamation_mark():
    assert assignment.add_exclamation_mark("hello") == "hello!"

def test_subtract_three_point_five():
    assert assignment.subtract_three_point_five(10) == 6.5

def test_multiply_by_five():
    assert assignment.multiply_by_five(10) == 50

def test_divide_by_seven():
    assert assignment.multiply_by_five(14) == 2
