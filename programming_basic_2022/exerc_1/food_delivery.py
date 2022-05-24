count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegetarian_menu = int(input())
chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
delivery = 2.50
price_chicken_menu = count_chicken_menu * chicken_menu
price_fish_menu = count_fish_menu * fish_menu
price_vegetarian_menu = count_vegetarian_menu * vegetarian_menu
total_price_without_delivery = price_chicken_menu + price_fish_menu + price_vegetarian_menu
price_dessert = total_price_without_delivery * 0.20
total_price = total_price_without_delivery + price_dessert + delivery
print(total_price)

