number_of_pages = int(input())
pages_for_hour =  int(input())
number_of_days = int(input())
total_hours = number_of_pages / pages_for_hour
hours_for_day = total_hours // number_of_days

print (hours_for_day)