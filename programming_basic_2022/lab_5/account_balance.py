payment = input()
total = 0
while payment != 'NoMoreMoney':
    increase = float(payment)
    if increase > 0:
        print(f'Increase: {increase:.2f}')
    if increase < 0:
        print('Invalid operation!')
        break
    total += increase
    payment = input()
print(f'Total: {total:.2f}')