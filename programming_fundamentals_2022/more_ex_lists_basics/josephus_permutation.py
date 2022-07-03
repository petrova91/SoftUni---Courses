people_in_circle = input().split()
number_of_executed_person = int(input())
order_of_executions = []
counter_executed_people = 0
while len(people_in_circle) > 0:
    for index, element in enumerate(people_in_circle):
        counter_executed_people += 1
        if counter_executed_people == number_of_executed_person:
            order_of_executions.append(element)
            people_in_circle.pop(index)
            counter_executed_people = 1
        if index == len(people_in_circle):
            index = 0
            counter_executed_people = 0
print(f'[{",".join(order_of_executions)}]') #премахва разстоянието между ',' и числото