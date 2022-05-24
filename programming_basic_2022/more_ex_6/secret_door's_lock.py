end_hundreds = int(input())
end_tens = int(input())
end_units = int(input())
for hundreds in range(2, end_hundreds+1, +2):
    for tens in range(2, end_tens+1):
        if tens == 2 or tens == 3 or tens == 5 or tens == 7:
            for units in range(2, end_units+1, +2):
                print(f'{hundreds} {tens} {units}')