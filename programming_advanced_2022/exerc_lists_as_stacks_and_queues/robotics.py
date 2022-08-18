from collections import deque


def printed_message(current_time, current_product, name_robot):
    current_time = current_time % (24 * 60 * 60)
    hh = current_time // 3600
    mm = ((current_time % 3600) // 60)
    ss = ((current_time % 3600) % 60)
    print(f"{name_robot} - {current_product} [{hh:02d}:{mm:02d}:{ss:02d}]")


sequence_of_robots = deque(input().split(";"))
robots_in_process = {}
robots_process_time = {}
hours, minutes, seconds = input().split(":")
time_in_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
timer = time_in_seconds
product = input()
products = deque()
while not product == "End":
    products.append(product)
    product = input()
while products:
    timer += 1
    current_product = products.popleft()
    if robots_in_process:
        for robot in robots_in_process:
            robots_in_process[robot] -= 1
    if sequence_of_robots:
        robot = sequence_of_robots.popleft()
        robot_name, process_time = robot.split("-")
        robots_in_process[robot_name] = int(process_time)
        robots_process_time[robot_name] = int(process_time)
        printed_message(timer, current_product, robot_name)
    else:
        for robot in robots_in_process:
            if robots_in_process[robot] <= 0:
                printed_message(timer, current_product, robot)
                robots_in_process[robot] = robots_process_time[robot]
                break
        else:
            products.append(current_product)




