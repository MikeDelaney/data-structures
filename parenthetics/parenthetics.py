import string


def check_parenthetics(a_string):
    if type(a_string) is not str:
        raise TypeError
    open_parens = string.count(a_string, '(')
    closed_parents = string.count(a_string, ')')
    if open_parens > closed_parents:
        return 1
    elif open_parens == closed_parents:
        return 0
    else:
        return -1
