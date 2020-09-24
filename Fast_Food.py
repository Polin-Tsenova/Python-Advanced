from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])
order_completed = True

print(max(orders))

while orders:
    current_order = orders.popleft()

    if food >= current_order:
        food -= current_order
    else:
        orders.appendleft(current_order)
        # print(f"Orders left: {' '.join([str(x) for x in list(orders)])}")
        order_completed = False
        break

if order_completed:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in list(orders)])}")


# Test Input
# 348
# 20 54 30 16 7 9

# 499
# 57 45 62 70 33 90 88 76