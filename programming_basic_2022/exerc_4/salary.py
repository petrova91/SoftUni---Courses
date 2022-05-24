count_website = int(input())
salary = int(input())
penalty_facebook = 150
penalty_instagram = 100
penalty_reddit = 50
for count_check in range(count_website):
    name_website = input()
    if name_website == 'Facebook':
        salary -= penalty_facebook
        if salary <= 0:
            print('You have lost your salary.')
            break
    if name_website == 'Instagram':
        salary -= penalty_instagram
        if salary <= 0:
            print('You have lost your salary.')
            break
    if name_website == 'Reddit':
        salary -= penalty_reddit
        if salary <= 0:
            print('You have lost your salary.')
            break
if salary <= 0:
    pass
else:
    print(salary)