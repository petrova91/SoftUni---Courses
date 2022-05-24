budget = float(input())
name_actor = input()
while name_actor != 'ACTION':
    length_name = len(name_actor)
    if length_name > 15:
        actor_salary = budget * 0.20
        budget -= actor_salary
    elif length_name <= 15:
        salary = float(input())
        budget -= salary
    if budget <= 0:
        break
    name_actor = input()
if budget >= 0:
    print(f'We are left with {abs(budget):.2f} leva.')
else:
    print(f'We need {abs(budget):.2f} leva for our actors.')