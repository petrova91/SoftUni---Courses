working_days_month = int(input())
money_earned_for_day = float(input())
course_dollar_lev = float(input())
money_earned_for_month = working_days_month * money_earned_for_day
money_earned_for_year = money_earned_for_month * 12
year_bonus = money_earned_for_month * 2.5
money_earned_for_year += year_bonus
money_earned_for_year -= money_earned_for_year * 0.25
average_money_earned_dollars = money_earned_for_year / 365
average_money_earned_leva = average_money_earned_dollars * course_dollar_lev
print(f'{average_money_earned_leva:.2f}')