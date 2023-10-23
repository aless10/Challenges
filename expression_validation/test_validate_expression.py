import pytest

from expression_validation.counter import validate_expression as validate_expression_counter
from expression_validation.stack import validate_expression as validate_expression_stack



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
    assert validate_expression_counter(input_exp) == expected


@pytest.mark.parametrize("input_exp, expected", [
    ("", True),
    ("()", True),
    (")(", False),
    ("(())", True),
    ("(()", False),
    ("())", False),
    ("(()())", True),
])
def test_stack(input_exp, expected):
    assert validate_expression_stack(input_exp) == expected


@pytest.mark.parametrize("input_exp, expected", [
    ("()[]{}", True),
    ("([{}])", True),
    ("[{]", False),
    ("([{})]", False),
])
def test_stack_multiple(input_exp, expected):
    assert validate_expression_stack(input_exp) == expected
