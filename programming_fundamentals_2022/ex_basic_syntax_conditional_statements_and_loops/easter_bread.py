budget = float(input())
price_flour = float(input())
number_of_loaves = 0
colored_eggs = 0
price_eggs = price_flour * 0.75
price_milk = price_flour * 1.25
price_one_loaf = (1 * price_eggs) + (1 * price_flour) + (0.250 * price_milk)
while budget > price_one_loaf:
    budget -= price_one_loaf
    colored_eggs += 3
    number_of_loaves += 1
    if number_of_loaves % 3 == 0:
        lost_eggs = number_of_loaves - 2
        colored_eggs -= lost_eggs
print(f'You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
