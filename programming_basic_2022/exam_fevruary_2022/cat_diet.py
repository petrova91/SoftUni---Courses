percent_fat = int(input())
percent_proteins = int(input())
percent_carbs = int(input())   # въглехидрати
total_calories = int(input())
percent_water = int(input())
gram_fat = 9
gram_proteins = 4
gram_carbs = 4
total_grams_fat = ((percent_fat / 100) * total_calories) / gram_fat
total_grams_proteins = ((percent_proteins / 100) * total_calories) / gram_proteins
total_grams_carbs = ((percent_carbs / 100) * total_calories) / gram_carbs
total_count_foot = total_grams_fat + total_grams_proteins + total_grams_carbs
calories_for_gram = total_calories / total_count_foot
count_calories = ((100 - percent_water) / 100) * calories_for_gram
print(f'{count_calories:.4f}')




