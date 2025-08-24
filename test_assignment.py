import pytest
import  assignment

def test_hello():
    assert assignment.hello_world() == "Hello World!"

    @pytest.mark.parametrize("input, expected", [
        ("Hello World", "hello world"),
        ("PYTHON", "python"),
        ("123ABC", "123abc"),
    ])
    def test_convert_to_lowercase_parametrize(input, expected):
        assert assignment.convert_to_lowercase(input) == expected

    @pytest.mark.parametrize("input, expected", [
        ("hello world", "HELLO WORLD"),
        ("python", "PYTHON"),
        ("123abc", "123ABC"),
    ])
    def test_convert_to_uppercase_parametrize(input, expected):
        assert assignment.convert_to_uppercase(input) == expected

    @pytest.mark.parametrize("input, expected", [
        ("hello world", "Hello World"),
        ("python programming", "Python Programming"),
        ("123abc", "123Abc"),
    ])
    def test_convert_to_titlecase_parametrize(input, expected):
        assert assignment.convert_to_titlecase(input) == expected

    @pytest.mark.parametrize("input, expected", [
        ("hello", "hello!"),
        ("python", "python!"),
        ("123abc", "123abc!"),
    ])
    def test_add_exclamation_mark_parametrize(input, expected):
        assert assignment.add_exclamation_mark(input) == expected

    @pytest.mark.parametrize("input, expected", [
        (10.5, 7.0),
        (0, -3.5),
        (-7, -10.5),
    ])
    def test_subtract_three_point_five_parametrize(input, expected):
        assert assignment.subtract_three_point_five(input) == expected

    @pytest.mark.parametrize("input, expected", [
        (2, 10),
        (0, 0),
        (-3, -15),
    ])
    def test_multiply_by_five_parametrize(input, expected):
        assert assignment.multiply_by_five(input) == expected

    @pytest.mark.parametrize("input, expected", [
        (14, 2),
        (7, 1),
        (0, 0),
    ])
    def test_divide_by_seven_parametrize(input, expected):
        assert assignment.divide_by_seven(input) == expected
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
    assert assignment.divide_by_seven(14) == 2
