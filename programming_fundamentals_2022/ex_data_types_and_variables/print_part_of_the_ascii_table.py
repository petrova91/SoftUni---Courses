start_letter = int(input())
stop_letter = int(input())
for current_letter in range(start_letter, stop_letter+1):
    print(f'{chr(current_letter)}', end=' ')