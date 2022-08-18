def header():
    return f"CASH RECEIPT\n------------------------------"


def body():
    return f"Charged to____________________\nReceived by___________________"


def footer():
    return f"------------------------------\n© SoftUni"


def blank_cash():
    print(header())
    print(body())
    print(footer())


blank_cash()
