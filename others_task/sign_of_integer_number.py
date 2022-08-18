def sign_number(num):
    if num == 0:
        return "zero"
    elif num > 0:
        return "positive"
    return "negative"


number = int(input())
print(f"The number {number} is {sign_number(number)}.")