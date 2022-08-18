algebraic_expression = input()
index_stack = []
for index in range(len(algebraic_expression)):
    if algebraic_expression[index] == "(":
        index_stack.append(index)
    elif algebraic_expression[index] == ")":
        start_index = index_stack.pop()
        math_expression = algebraic_expression[start_index:index+1]
        print(math_expression)