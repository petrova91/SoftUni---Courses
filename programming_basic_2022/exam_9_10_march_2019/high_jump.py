desired_height = int(input())
count_jumps_from_start = 0
start_height = desired_height - 30
he_is_fail = False
count_current_jumps = 0
last_height = ''
while start_height <= desired_height:
    jump_height = int(input())
    count_jumps_from_start += 1
    if jump_height > start_height:
        start_height += 5
        count_current_jumps = 0
        last_height = start_height - 5
    elif jump_height <= start_height:
        count_current_jumps += 1
        if count_current_jumps == 3:
            he_is_fail = True
            break
        else:
            continue
if he_is_fail:
    print(f'Tihomir failed at {start_height}cm after {count_jumps_from_start} jumps.')
else:
    print(f'Tihomir succeeded, he jumped over {last_height}cm after {count_jumps_from_start} jumps.')