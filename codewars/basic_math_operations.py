def basic_op(operator, value1, value2):
    if operator == '+':
        action = value1 + value2
    elif operator == '-':
        action = value1 - value2
    elif operator == '*':
        action = value1 * value2
    else:
        action = value1 / value2
    return action