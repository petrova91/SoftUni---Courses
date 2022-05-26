from forex_python.converter import CurrencyRates

amount = int(input())
c = CurrencyRates()
current_rate = c.get_rate('GBP', 'USD')
result = current_rate * amount
print(f'{result}')

# импортира текущият курс на исканата валута