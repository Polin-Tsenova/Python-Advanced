from collections import deque

n = int(input())
circle = deque({})
pump_dict = {}

for i in range(0, n ):
    pump = input().split()
    amount = int(pump[0])
    distance = int(pump[1])
    pump_dict[amount] = distance

circle.append(pump_dict)

print(circle)