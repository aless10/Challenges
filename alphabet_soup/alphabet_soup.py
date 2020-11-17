"""
    Alphabet Soup
    =============

    Everyone loves alphabet soup. 
    And of course, you want to know if you can construct a message from the letters found in your bowl. 
    Your Task: Write a function that takes as input two strings:
        - the message you want to write
        - all the letters found in your bowl of alphabet soup.
    Assumptions:
        - It may be a very large bowl of soup containing many letters.
        - There is no guarantee that each letter occurs a similar number of times - indeed some letters might be missing entirely.
        - The letters are ordered randomly.
    
    The function should determine if you can write your message with the letters found in your bowl of soup. 
    The function should return True or False accordingly. Try to make your function efficient.  
    Please use Big-O notation to explain how long it takes your function to run in terms of the length of your 
    message (m) and the number of letters in your bowl of soup (s).

    Examples:

    >>> is_it_a_good_soup("yes", "yyeess")
    True
    >>> is_it_a_good_soup("no", "yyeess")
    False

    Time Complexity:
        - Counter on message -> m = len(message)
        - Counter on soup -> s = len(soup)
        - for loop -> m = len(message)
    so the time complexity of this solution should be
        O(2m+s) ~ O(m+s)

"""

from collections import Counter


def is_it_a_good_soup(message: str, soup: str) -> bool:
    m = Counter(filter(lambda x: x.isalpha(), list(message)))
    s = Counter(list(soup))
    for k, v in m.items():
        if v > s[k]:
            return False
    return True
