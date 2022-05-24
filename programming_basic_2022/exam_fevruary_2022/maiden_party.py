price_maiden_party = float(input())
count_love_message = int(input())
count_waxy_roses = int(input())
count_keychains = int(input())
count_cartoons = int(input())
count_lucky = int(input())
price_love_message = 0.60
price_waxy_rose = 7.20
price_keychain = 3.60
price_cartoon = 18.20
price_lucky = 22
hosting = 0.1
total_win = (count_love_message * price_love_message) + (count_waxy_roses * price_waxy_rose) + \
              (count_keychains * price_keychain) + (count_cartoons * price_cartoon) + \
              (count_lucky * price_lucky)
counter_products = count_love_message + count_waxy_roses + count_keychains + count_cartoons + count_lucky
if counter_products >= 25:
    total_win *= 0.65
total_win -= total_win * hosting
different = abs(total_win - price_maiden_party)
if total_win >= price_maiden_party:
    print(f'Yes! {different:.2f} lv left.')
else:
    print(f'Not enough money! {different:.2f} lv needed.')