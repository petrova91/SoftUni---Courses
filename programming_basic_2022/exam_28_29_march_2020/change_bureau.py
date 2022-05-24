count_bitcoins = int(input())
count_chinese_yuan = float(input())
percent_commission = float(input())
one_bitcoin_leva = 1168
one_chinese_yuan_dollar = 0.15
one_dollar_leva = 1.76
one_euro_leva = 1.95
total_leva = (count_bitcoins * one_bitcoin_leva) + ((count_chinese_yuan * one_chinese_yuan_dollar) * one_dollar_leva)
total_euro = total_leva / one_euro_leva
commission = total_euro * (percent_commission / 100)
total_euro -= commission
print(f'{total_euro:.2f}')