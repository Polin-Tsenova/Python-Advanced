from collections import deque

green_light = int(input())
free_window = int(input())

crossroads = deque()
total_cars_passed = 0
is_crash = False
crashed_car = ''
hit_element = ''



while True:
    command = input()
    if command == "END":
        break
    if command == 'green':
        green = green_light
        free = free_window
        while True:
            if crossroads:
                car = crossroads.popleft()
                if green > len(car):
                    green -= len(car)
                    total_cars_passed += 1
                elif green + free > len(car):
                    total_cars_passed += 1
                    break
                elif green + free < len(car):
                    hit_element = car[green + free]
                    crashed_car = car
                    is_crash= True
                    break
            else:
                break
    else:
        crossroads.append(command)


if is_crash:
    print("A crash happened!")
    print(f"{crashed_car} was hit at {hit_element}.")
else:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")

