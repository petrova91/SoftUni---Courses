count_junior_bikers = int(input())
count_seniors_bikers = int(input())
type_of_road = input()
tax_junior = 0
tax_senior = 0
if type_of_road == 'trail':
    tax_junior = 5.50
    tax_senior = 7
elif type_of_road == 'cross-country':
    tax_junior = 8
    tax_senior = 9.50
elif type_of_road == 'downhill':
    tax_junior = 12.25
    tax_senior = 13.75
elif type_of_road == 'road':
    tax_junior = 20
    tax_senior = 21.50
collected_money = count_junior_bikers * tax_junior + count_seniors_bikers * tax_senior
if type_of_road == 'cross-country' and count_seniors_bikers + count_junior_bikers >= 50:
    collected_money *= 0.75
collected_money *= 0.95
print(f'{collected_money:.2f}')