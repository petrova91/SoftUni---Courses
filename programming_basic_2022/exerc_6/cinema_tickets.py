name_movie = input()
count_tickets = 0
count_student_ticket = 0
count_standard_ticket = 0
count_kid_ticket = 0
while name_movie != 'Finish':
    count_free_places = int(input())
    total_places = count_free_places
    type_ticket = input()
    count_sold_tickets = 0
    while type_ticket != 'End':
        if type_ticket == 'student':
            count_student_ticket += 1
            count_tickets += 1
            count_sold_tickets += 1
            total_places -= 1
        elif type_ticket == 'standard':
            count_tickets += 1
            count_standard_ticket += 1
            count_sold_tickets += 1
            total_places -= 1
        elif type_ticket == 'kid':
            count_tickets += 1
            count_kid_ticket += 1
            count_sold_tickets += 1
            total_places -= 1
        if total_places <= 0:
            break
        type_ticket = input()
    percent_full_hall = (count_sold_tickets / count_free_places) * 100
    print(f'{name_movie} - {percent_full_hall:.2f}% full.')
    name_movie = input()
percent_student_tickets = (count_student_ticket / count_tickets) * 100
percent_standard_tickets = (count_standard_ticket / count_tickets) * 100
percent_kid_tickets = (count_kid_ticket / count_tickets) * 100
print(f'Total tickets: {count_tickets}')
print(f'{percent_student_tickets:.2f}% student tickets.')
print(f'{percent_standard_tickets:.2f}% standard tickets.')
print(f'{percent_kid_tickets:.2f}% kids tickets.')
