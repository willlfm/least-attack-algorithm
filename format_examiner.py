def remove_spaces(input_string):
    no_spaces_string = input_string.replace(" ", "")
    return no_spaces_string


def is_well_formed_formula(input_str):
    stack = []
    operators = ['¬', '∧', '∨', '→', '↔']
    input_str = remove_spaces(input_str)

    i = 0
    for char in input_str:
        if char == '(':
            if input_str[i + 1] == ')':
                return False
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
        elif char in operators:
            if char == '¬':
                if i < len(input_str) - 1 and (input_str[i + 1].isalpha() or input_str[i + 1] == '('):
                    pass
                else:
                    return False
            elif i == 0 or i == len(input_str) - 1:
                return False
            elif input_str[i + 1] in operators:
                return False
        elif char.isalpha():
            if i < len(input_str) - 1 and input_str[i + 1].isalpha():
                return False
        i += 1
    if stack:
        return False
    else:
        return True


def main():
    test_cases = [
        "()",  # false
        "p",  # true
        "(p∧q)",  # true
        "q)",  # false
        "¬q",
        "¬q∧p",
        "pp",
        "¬(¬a)"
    ]
    for test_case in test_cases:
        result = is_well_formed_formula(test_case)
        print(f"{test_case} : {result}")


if __name__ == "__main__":
    main()
