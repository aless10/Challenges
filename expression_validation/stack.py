OPENING = {
    "(": ")",
    "[": "]",
    "{": "}"
}


def validate_expression(_input_exp: str) -> bool:
    if len(_input_exp) == 0:
        return True
    stack = []
    index = 0
    exp_len = len(_input_exp)
    while index < exp_len:
        current = _input_exp[index]
        if current in OPENING:
            stack.append(current)
        else:
            if stack:
                last = stack.pop()
                if OPENING[last] != current:
                    return False
            else:
                return False
        index += 1
    return len(stack) == 0
