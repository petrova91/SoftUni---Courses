current_year = int(input())
happy_year_condition = False
while not happy_year_condition:
    current_year += 1
    set_year = set()
    for i in range(len(str(current_year))):
        set_year.add(str(current_year)[i])
    happy_year_condition = len(set_year) == len(str(current_year))
print(current_year)