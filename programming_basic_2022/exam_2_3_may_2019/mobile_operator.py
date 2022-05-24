period_of_contract = input()
type_of_contract = input()
mobile_internet = input()
count_months = int(input())
monthly_tax = 0
if period_of_contract == 'one':
    if type_of_contract == 'Small':
        monthly_tax = 9.98
    elif type_of_contract == 'Middle':
        monthly_tax = 18.99
    elif type_of_contract == 'Large':
        monthly_tax = 25.98
    elif type_of_contract == 'ExtraLarge':
        monthly_tax = 35.99
elif period_of_contract == 'two':
    if type_of_contract == 'Small':
        monthly_tax = 8.58
    elif type_of_contract == 'Middle':
        monthly_tax = 17.09
    elif type_of_contract == 'Large':
        monthly_tax = 23.59
    elif type_of_contract == 'ExtraLarge':
        monthly_tax = 31.79
if mobile_internet == 'yes':
    if monthly_tax <= 10.00:
        monthly_tax += 5.50
    elif monthly_tax <= 30.00:
        monthly_tax += 4.35
    elif monthly_tax > 30:
        monthly_tax += 3.85
total_bill = count_months * monthly_tax
if period_of_contract == 'two':
    total_bill -= total_bill * (3.75 / 100)
print(f'{total_bill:.2f} lv.')