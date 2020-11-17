import string

import pytest

from alphabet_soup.alphabet_soup import is_it_a_good_soup


@pytest.mark.parametrize(("message", "soup", "expected"), [
    ("yes", "yyeess", True),
    ("no", "yyeess", False),
    ("i am", "iam", True),
    ("i\nam", "iam", True),
    ("the quick brown fox jumps over the lazy dog", string.ascii_lowercase, False)
])
def test_good_soup(message, soup, expected):
    assert is_it_a_good_soup(message, soup) is expected
