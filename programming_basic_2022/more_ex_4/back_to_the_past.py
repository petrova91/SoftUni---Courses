legacy = float(input())
year_of_living = int(input())
real_ages = 18
for current_years in range(1800, year_of_living +1):
    if current_years % 2 == 0:
        legacy -= 12000
    else:
        legacy -= 12000 + (50 * real_ages)
    real_ages += 1
if legacy >= 0:
    print(f'Yes! He will live a carefree life and will have {legacy:.2f} dollars left.')
else:
    legacy = abs(legacy)
    print(f'He will need {legacy:.2f} dollars to survive.')

