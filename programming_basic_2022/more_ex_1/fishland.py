price_mackerel_kg = float(input()) #скумрия
price_sprat_kg = float(input())    #цаца
bonito_kg = float(input())         #паламуд
safrid_kg = float(input())         #сафрид
mussels_kg = int(input())          #миди
price_bonito = price_mackerel_kg * 0.60 + price_mackerel_kg
price_safrid = price_sprat_kg + price_sprat_kg * 0.80
price_mussels = 7.50
total_bonito = bonito_kg * price_bonito
total_safrid = safrid_kg * price_safrid
total_mussels = mussels_kg * price_mussels
total_sum = total_bonito + total_safrid + total_mussels
#print(round(total_sum,2))
print(f'{total_sum:.2f}')