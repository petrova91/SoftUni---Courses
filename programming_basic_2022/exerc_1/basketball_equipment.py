year_tax = int(input())
#Баскетболни кецове – цената им е 40% по-малка от таксата за една година
shoes = year_tax - year_tax * 0.40
#Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
clothes = shoes - shoes * 0.20
#Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
ball = clothes / 4
#Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка
accessory = ball / 5
cost = year_tax + shoes + clothes + ball + accessory
print (cost)