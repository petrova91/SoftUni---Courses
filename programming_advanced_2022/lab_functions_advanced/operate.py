import functools, operator


def operate(sign, *args):
    if sign == "+":
        return functools.reduce(operator.add, args)
    elif sign == "-":
        return functools.reduce(operator.sub, args)
    elif sign == "*":
        return functools.reduce(operator.mul, args)
    elif sign == "/":
        return functools.reduce(operator.truediv, args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
