population = input().split(', ')
min_wealth = int(input())
population_list = [int(element) for element in population]
not_enough_money = False
for i in range(len(population_list)):
    max_value_wealth = max(population_list)
    index_max_value = population_list.index(max_value_wealth)
    different = 0
    if population_list[i] == min_wealth:
        continue
    elif population_list[i] < min_wealth < max_value_wealth:
        different = min_wealth - population_list[i]
        population_list[index_max_value] -= different
        population_list[i] += different
    if max_value_wealth <= min_wealth:
        not_enough_money = True
        break
if not_enough_money:
    print('No equal distribution possible')
else:
    print(population_list)
