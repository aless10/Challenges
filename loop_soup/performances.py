import string
import timeit
from loop_soup.alphabet_soup import is_it_a_good_soup_review, is_it_a_good_soup

MESSAGE = "the quick brown fox jumps over the lazy dog"

SOUP = string.ascii_letters * 100


def calculate_execution_time(fn, iterations=10000):
    result = timeit.timeit(lambda: fn(MESSAGE, SOUP), number=iterations)
    print(f"The function {fn.__name__} tooks {result} seconds")
    return result


def main():
    counter_version = calculate_execution_time(is_it_a_good_soup)
    iter_version = calculate_execution_time(is_it_a_good_soup_review)
    if counter_version > iter_version:
        print(f"{is_it_a_good_soup_review.__name__} is faster")
    else:
        print(f"{is_it_a_good_soup.__name__} is faster")


if __name__ == "__main__":
    main()
