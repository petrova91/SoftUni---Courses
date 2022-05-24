from math import pi

figurе = input ()
if figurе == 'square':
    number_a = float(input())
    area = number_a * number_a
    print(f'{area:.3f}')
elif figurе == 'rectangle':
    number_a = float(input())
    number_b = float(input())
    area = number_a * number_b
    print(f'{area:.3f}')
elif figurе == 'circle':
    r = float(input())
    area = pi * r * r
    print(f'{area:.3f}')
elif figurе == 'triangle':
    number_a = float(input())
    number_h = float(input())
    area = (number_a * number_h) / 2
    print(f'{area:.3f}')

