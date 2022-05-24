price_t_shirt = float(input())
sum_to_win_ball = float(input())
price_shorts = price_t_shirt * 0.75
price_socks = price_shorts * 0.20
price_buttons = (price_t_shirt + price_shorts) * 2
total_bill = price_t_shirt + price_shorts + price_socks + price_buttons
total_bill -= total_bill * 0.15
if total_bill >= sum_to_win_ball:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total_bill:.2f} lv.')
else:
    different = sum_to_win_ball - total_bill
    print('No, he will not earn the world-cup replica ball.')
    print(f'He needs {different:.2f} lv. more.')