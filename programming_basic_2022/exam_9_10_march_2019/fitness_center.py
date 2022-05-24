total_count_people = int(input())
count_people_back = 0
count_people_chest = 0
count_people_legs = 0
count_people_abs = 0
count_people_buy_protein_shake = 0
count_people_buy_protein_bar = 0
count_training_people = 0
count_shopping_people = 0
for current_person in range(1, total_count_people + 1):
    activity = input()
    if activity == 'Back':
        count_people_back += 1
        count_training_people += 1
    elif activity == 'Chest':
        count_people_chest += 1
        count_training_people += 1
    elif activity == 'Legs':
        count_people_legs += 1
        count_training_people += 1
    elif activity == 'Abs':
        count_people_abs += 1
        count_training_people += 1
    elif activity == 'Protein shake':
        count_people_buy_protein_shake += 1
        count_shopping_people += 1
    elif activity == 'Protein bar':
        count_people_buy_protein_bar += 1
        count_shopping_people += 1
percent_training_people = (count_training_people / total_count_people) * 100
percent_shopping_people = (count_shopping_people / total_count_people) * 100
print(f'{count_people_back} - back')
print(f'{count_people_chest} - chest')
print(f'{count_people_legs} - legs')
print(f'{count_people_abs} - abs')
print(f'{count_people_buy_protein_shake} - protein shake')
print(f'{count_people_buy_protein_bar} - protein bar')
print(f'{percent_training_people:.2f}% - work out')
print(f'{percent_shopping_people:.2f}% - protein')

