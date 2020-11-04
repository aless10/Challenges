"""
    Reverse Polish Notation
    =======================

    Implement a function that calculates a mathematical expression in
    reverse polish notation (RPN).

    RPN is stack oriented, knows integers and the operators +, -, *, /.
    Words (an integer or operator) are separated by a single space. Words
    should be evaluated from left to right.

    Integers are pushed to a stack. Operators pop their operands from the
    stack and push the result onto the stack. If the stack doesn't have enough
    potential operands on it, an exception should be raised.

    If the expression is fully evaluated the stack should have exactly one
    element, this is the result. If there is more than one element, an
    exception should be raised.

    Examples:

    >>> calculate("1 1 +")
    2
    >>> calculate("1 1 1 +")
    ERROR
    >> calculate("1 1 1 + +")
    3
    >>> calculate("1 1 1 + -")
    1
    >>> calculate("1 1 + 1 +")
    3
    >>> calculate("4 2 /")
    2
    >>> calculate("1 1")
    ERROR
    >>> calculate("1 + 1")
    ERROR
"""

import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def calculate(expression: str) -> int:
    integer_counter = 0
    operators_counter = 0
    integer_stack = []
    expression_list = expression.split(" ")
    for symbol in expression_list:
        try:
            integer_stack.append(int(symbol))
            integer_counter += 1
        except ValueError:
            operators_counter += 1
            last = integer_stack.pop()
            second_to_last = integer_stack.pop()
            integer_stack.insert(0, ops.get(symbol)(second_to_last, last))

    if integer_counter != operators_counter + 1:
        # TODO: put this in a validation function
        raise Exception("The string was not well formatted")
    return integer_stack[0]
