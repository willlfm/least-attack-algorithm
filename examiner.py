def is_valid_math_expression(expression):

    # 去除空格
    expression = expression.replace(" ", "")

    # 检查括号匹配
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    if stack:
        return False

    # 检查运算符位置
    operators = set('+-*/')
    for i, char in enumerate(expression):
        if char in operators:
            if i == 0 or i == len(expression) - 1:
                return False
            if expression[i - 1] in operators or expression[i + 1] in operators:
                return False

    # 检查连续运算符
    for i in range(len(expression) - 1):
        if expression[i] in operators and expression[i + 1] in operators:
            return False

    # 检查除数不为0
    for i, char in enumerate(expression):
        if char == '/':
            if i == len(expression) - 1 or expression[i + 1] == '0':
                return False

    return True


# 测试示例
expressions = [
    "1+1",
    "1+(1/2)",
    "1++1",
    "(1+2)",
    "(1+2",
    "1/0"
]

for expression in expressions:
    print(f"表达式 '{expression}' 是{'合格' if is_valid_math_expression(expression) else '不合格'}的。")
