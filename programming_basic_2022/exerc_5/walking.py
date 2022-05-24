goal_steps = 10000
goal_is_reached = True
while goal_steps >= 0:
    command = input()
    if command == 'Going home':
        steps_to_go_home = int(input())
        goal_steps -= steps_to_go_home
        if goal_steps > 0:
            goal_is_reached = False
        break
    current_steps = int(command)
    goal_steps -= current_steps
if goal_is_reached:
    print(f'Goal reached! Good job!')
    print(f'{abs(goal_steps)} steps over the goal!')
else:
    print(f'{goal_steps} more steps to reach goal.')