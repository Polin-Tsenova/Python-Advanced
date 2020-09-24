from collections import deque

numbers = [int(x) for x in input().split()]
enqueue, dequeue, searched_number = numbers

queue = deque([int(x) for x in input().split()])[:enqueue]

[queue.popleft() for _ in range(dequeue)]

if searched_number in queue:
    print("True")
else:
    if queue:
        print(min(queue))
    else:
        print('0')

# Test input
# 5 2 32
# 1 13 45 32 4

# 3 3 90
# 90 0 90

# 4 1 666
# 666 69 13 420