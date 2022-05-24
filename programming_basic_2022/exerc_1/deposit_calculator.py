#сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

amount_deposited = float (input())       #депозирана сума
period_in_months = int (input())         #срок на депозита
annual_interest_rate = float (input())   #годишен лихвен процент
month_percentage = (amount_deposited * annual_interest_rate / 12)/100
total_sum = amount_deposited + period_in_months * month_percentage
print (total_sum)
