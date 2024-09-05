import pytest

from main import add


class TestAddFunction:

    def test_add_function_three_digits(self):
        response = add('1,2,3')
        assert response == 6

    def test_add_function_empty_string(self):
        response = add('')
        assert response == 0

    def test_add_function_signle_digit(self):
        response = add('3')
        assert response == 3

    def test_add_with_different_delimiters(self):
        response = add('1\n2,3')
        assert response == 6

    def test_support_multiple_delimieters(self):
        response = add('//;\n1;2;3')
        assert response == 6

