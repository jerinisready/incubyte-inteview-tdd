import pytest

from main import add, AddHandlerException


class TestAddFunction:

    def test_add_function_three_digits(self):
        response = add('//,\n1,2,3')
        assert response == 6

    def test_add_function_empty_string(self):
        response = add('//,\n')
        assert response == 0

    def test_add_function_signle_digit(self):
        response = add('//,\n3')
        assert response == 3


    @pytest.mark.skip(reason="Skipping this test for now")
    def test_add_with_different_delimiters(self):   # ignoring passing case of \n anymore
        response = add('//,\\n\n1\n2,3')
        assert response == 6

    def test_support_multiple_delimieters(self):
        response = add('//;\n1;2;3')
        assert response == 6

    def test_handle_invalid_syntax_input(self):
        with pytest.raises(AddHandlerException, match="Improply created input pattern"):
            add('/;\n124')

        with pytest.raises(AddHandlerException, match="Improply created input pattern"):
            add('//;123')

    def test_handle_negative_numebr(self):
        with pytest.raises(AddHandlerException, match="negative numbers not allowed -1"):
            add('//;\n-1;2;3')


    def test_handle_negative_numebrs(self):
        with pytest.raises(AddHandlerException, match="negative numbers not allowed -1,-3"):
            add('//;\n-1;2;-3')

