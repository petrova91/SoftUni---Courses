w_m = float(input())   #дължина
h_m = float(input())    #широчина
w_cm = w_m * 100
h_cm = h_m * 100
work_place_w_cm = 120
work_place_h_cm = 70
corridor_cm = 100
count_places = (w_cm // work_place_w_cm) * ((h_cm - corridor_cm)// work_place_h_cm) - 3
print (count_places)