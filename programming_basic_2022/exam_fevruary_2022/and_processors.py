import math

count_processors = int(input())
count_workers = int(input())
count_days = int(input())
making_hours = 3
working_hours = 8
price_processors = 110.10
count_making_processors = math.floor((count_workers * count_days * working_hours) / 3)
different = abs(count_processors - count_making_processors)
money_different = different * price_processors
if count_processors <= count_making_processors:
    print(f'Profit: -> {money_different:.2f} BGN')
else:
    print(f'Losses: -> {money_different:.2f} BGN')