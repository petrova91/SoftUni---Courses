count_days = int(input())
total_raised_money = 0
total_wins = 0
total_losses = 0
for current_day in range(count_days):
    sport = input()
    wins = 0
    losses = 0
    raised_money_for_current_day = 0
    while sport != 'Finish':
        result = input()
        if result == 'win':
            raised_money_for_current_day += 20
            wins += 1
            total_wins += 1
        else:
            losses += 1
            total_losses += 1
        sport = input()
    if wins > losses:
        raised_money_for_current_day += raised_money_for_current_day * 0.10
    total_raised_money += raised_money_for_current_day
if total_wins > total_losses:
    total_raised_money += total_raised_money * 0.20
    print(f'You won the tournament! Total raised money: {total_raised_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_raised_money:.2f}')
