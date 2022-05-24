price_luggage = float(input())
weight_luggage = float(input())
days_before_traveling = int(input())
count_luggage = int(input())
if weight_luggage < 10:
    price_luggage *= 0.2
elif weight_luggage <= 20:
    price_luggage *= 0.5
else:
    price_luggage *= 1
if days_before_traveling > 30:
    price_luggage *= 1.10
elif 7 <= days_before_traveling <= 30:
    price_luggage *= 1.15
elif days_before_traveling < 7:
    price_luggage*= 1.40
total_price_luggage = price_luggage * count_luggage
print(f'The total price of bags is: {total_price_luggage:.2f} lv.')