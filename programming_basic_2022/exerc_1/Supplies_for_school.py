count_pens = int(input())
count_marker = int(input())
litter_detergent = int(input())
percent_discount = int(input())
price_pens = 5.80
price_marker = 7.20
price_detergent = 1.20
total_price_pens = count_pens * price_pens
total_price_marker = count_marker * price_marker
total_price_detergent = litter_detergent * price_detergent
total_price = total_price_pens + total_price_marker + total_price_detergent
total_price_discount = total_price - total_price*percent_discount/100
print (total_price_discount)
