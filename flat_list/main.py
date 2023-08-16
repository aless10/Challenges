# 1. write a function that returns all odd numbers in the given list
# all of the elements are integers or a list of integers
#
def odds_filters(input_list: list) -> list:
    result = []
    for element in input_list:
        if isinstance(element, int):
            if element % 2:
                result.append(element)
        else:
            result.extend(odds_filters(element))
    return result


l1 = [19, [51, 4], [19, [3, 8]], 42, [4, [90, [16, [6, 2], 3, 4]]]]
assert odds_filters(l1) == [19, 51, 19, 3, 3]


# 2. write a function that returns a set containing all numeric values in the given list that are duplicate
from collections import defaultdict


def find_duplicates(input_list: list, counter: dict | None = None) -> dict:
    if counter is None:
        counter = defaultdict(int)
    for element in input_list:
        if isinstance(element, int):
            counter[element] += 1
        else:
            find_duplicates(element, counter)

    return counter


def filter_duplicate(d: dict) -> set:
    return {k for k, v in d.items() if v > 1}


def find_duplicate_for_real(input_list: list) -> set:
    c = find_duplicates(input_list)
    return filter_duplicate(c)


l2 = [19, [51, 4], [19, [3, 8]], 42, [4, [90, [16, [6, 2], 3, 4]]]]
assert find_duplicate_for_real(l2) == {19, 3, 4}
