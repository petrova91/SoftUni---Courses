end_sector = input()
count_row_in_first_sector = int(input())
count_seats_odd_row = int(input())
total_count_seats = 0
start_sector = 'A'
start_number_seats = 'a'
end_number_seats_in_odd_row = ord(start_number_seats) + count_seats_odd_row
for current_sector in range(ord(start_sector), ord(end_sector) + 1):
    for current_row in range(1, count_row_in_first_sector + 1):
        if current_row % 2 == 1:
            for current_seats in range(ord(start_number_seats), end_number_seats_in_odd_row):
                total_count_seats += 1
                print(f'{chr(current_sector)}{current_row}{chr(current_seats)}')
        else:
            end_count_seats_even_row = end_number_seats_in_odd_row + 2
            for current_seats in range(ord(start_number_seats), end_count_seats_even_row):
                total_count_seats += 1
                print(f'{chr(current_sector)}{current_row}{chr(current_seats)}')
    count_row_in_first_sector += 1
print(f'{total_count_seats}')
