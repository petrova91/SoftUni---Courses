count_free_places = int(input())
price_tickets = 5
total_win = 0
current_win = 0
while count_free_places >= 0:
    incoming_people = input()
    if incoming_people == 'Movie time!':
        print(f'There are {count_free_places} seats left in the cinema.')
        break
    else:
        count_people = int(incoming_people)
        if count_people > count_free_places:
            print('The cinema is full.')
            break
        else:
            count_free_places -= count_people
            current_win = count_people * price_tickets
            if count_people % 3 == 0:
                current_win -= 5
            total_win += current_win
print(f'Cinema income - {total_win:.0f} lv.')