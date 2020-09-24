box = list(map(int,input().split()))
capacity = int(input())
sum = 0
rack = 1

while box:
    if sum + box[-1] <= capacity:
        cloth = box.pop()
        sum += cloth
    else:
        rack += 1
        sum = 0

print(rack)