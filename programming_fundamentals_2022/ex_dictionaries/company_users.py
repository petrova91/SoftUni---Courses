company_info = input().split(' -> ')
company_users = {}
while 'End' not in company_info:
    company_name = company_info[0]
    employee_id = company_info[1]
    if company_name not in company_users:
        company_users[company_name] = []
    if employee_id not in company_users[company_name]:
        company_users[company_name].append(employee_id)
    company_info = input().split(' -> ')
for company, employees in company_users.items():
    print(f'{company}')
    for current_employee_id in employees:
        print(f'-- {current_employee_id}')

