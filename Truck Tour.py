from collections import deque

n = int(input())
tank = deque()


for i in range(0, n):
    pump = [int(x) for x in input().split()]
    tank.append(pump)

for p in range(n):
    is_valid = True
    fuel = 0
    for _ in range(n):
        current = tank.popleft()
        fuel += current[0] - current[1]
        if fuel < 0:
            is_valid = False
        tank.append(current)
    if is_valid:
        print(p)
        break
    tank.append(tank.popleft())


