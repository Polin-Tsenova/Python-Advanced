from collections import deque

food = int(input())
queue = deque(map(int, input().split()))
print(max(queue))
order_completed = True

while queue:
    order = queue.popleft()

    if food >= order:
        food -= order
    else:
        queue.appendleft(order)
        order_completed = False
        break


if not order_completed:
    print(f"Orders left: {' '.join(map(str,queue))}")
else:
    print("Orders complete")
