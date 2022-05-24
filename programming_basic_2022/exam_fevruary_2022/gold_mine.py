count_locations = int(input())
for current_location in range(count_locations):
    average_yield_gold = float(input())
    count_days = int(input())
    yield_gold = 0
    for current_day in range(count_days):
        yield_gold_for_day = float(input())
        yield_gold += yield_gold_for_day
    average_yield_for_location = yield_gold / count_days
    if average_yield_for_location >= average_yield_gold:
        print(f'Good job! Average gold per day: {average_yield_for_location:.2f}.')
    else:
        different = average_yield_gold - average_yield_for_location
        print(f'You need {different:.2f} gold.')