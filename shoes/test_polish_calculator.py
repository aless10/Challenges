import pytest

from .polish_calculator import calculate


def test_simple_calculate():
    s = "1 1 +"
    assert calculate(s) == 2


def test_too_many_integers():
    s = "1 1 1 +"
    with pytest.raises(Exception):
        calculate(s)


def test_3_integers():
    s = "1 1 1 + +"
    assert calculate(s) == 3


def test_3_integers_with_minus():
    s = "1 1 1 + -"
    assert calculate(s) == 1


#     >> calculate("1 1 1 + +")
#     # []         1 1 1 + +
#     # [1]        1 1 + +
#     # [1, 1]     1 + +
#     # [1, 1, 1]  + +
#     # [1, 2]     +
#     # [3]
#     3
def test_3_integers_with_plus_inside():
    s = "1 1 + 1 +"
    assert calculate(s) == 3


#     >>> calculate("1 1 + 1 +")
#     # []         1 1 + 1 +
#     # [1]        1 + 1 +
#     # [1, 1]     + 1 +
#     # [2]        1 +
#     # [2, 1]     +
#     # [3]
#     3
def test_division():
    s = "4 2 /"
    assert calculate(s) == 2

#     >>> calculate("4 2 /")
#     2
#     >>> calculate("1 1")
#     ERROR


def test_no_operators():
    s = "1 1"
    with pytest.raises(Exception):
        calculate(s)


def test_bad_sorting():
    s = "1 + 1"
    with pytest.raises(Exception):
        calculate(s)

#     >>> calculate("1 + 1")
#     ERROR
