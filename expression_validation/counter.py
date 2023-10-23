def validate_expression(_input_exp: str) -> bool:
    counter = 0
    for c in _input_exp:
        if c == "(":
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            return False
    return counter == 0
