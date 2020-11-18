import string

import pytest

from .alphabet_soup import is_it_a_good_soup, is_it_a_good_soup_review

TEST_CASES = [
    ("yes", "yyeess", True),
    ("no", "yyeess", False),
    ("i am", "iam", True),
    ("i\nam", "iam", True),
    ("the quick brown fox jumps over the lazy dog", string.ascii_lowercase, False)
]


@pytest.mark.parametrize(("message", "soup", "expected"), TEST_CASES)
def test_good_soup(message, soup, expected):
    assert is_it_a_good_soup(message, soup) is expected


@pytest.mark.parametrize(("message", "soup", "expected"), TEST_CASES)
def test_good_soup_review(message, soup, expected):
    assert is_it_a_good_soup_review(message, soup) is expected
