import pytest

from expression_validation.counter import validate_expression


@pytest.mark.parametrize("input_exp, expected", [
    ("", True),
    ("()", True),
    (")(", False),
    ("(())", True),
    ("(()", False),
    ("())", False),
    ("(()())", True),
])
def test_counter(input_exp, expected):
    assert validate_expression(input_exp) == expected
