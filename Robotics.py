from collections import deque
from datetime import datetime, timedelta

robots = input().split(';')
robots_dict = {}

for el in range(len(robots)):
    robot, time = robots[el].split('-')
    robots_dict[el] = {
        'name': robot,
        'processing_time': int(time),
        'available_at': 0
    }

start_time = datetime.strptime(input(), '%H:%M:%S')

items = deque()

while True:
    command = input()
    if command == "End":
        break
    else:
        product = command
        items.append(product)

current_time = 0

while items:
    current_time += 1

    next_item = items.popleft()

    for robot in robots_dict:
        print(robot)
        if robot['available_at'] <= current_time:
            robot['available_at'] = current_time + robot['processing_time']
            robot_name = robot['name']
            time_str = (start_time + timedelta(seconds=current_time))\
                            .strftime('%H:%M:%S')
            print(f'{robot_name} - {next_item}[{time_str}]')
            break
    else:
        items.append(next_item)

