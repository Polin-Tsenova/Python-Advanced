from collections import deque

cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))

wasted_water = 0
is_remaining_bottles = True
is_remaining_cups = True

while True:
    if not bottles:
        is_remaining_bottles = False
        break
    if not cups:
        is_remaining_cups = False
        break
    current_cup = cups.popleft()
    current_bottle = bottles.pop()
    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
    elif current_bottle < current_cup:
        while True:
            if current_bottle >= current_cup:
                wasted_water += current_bottle - current_cup
                break
            current_cup -= current_bottle
            current_bottle = bottles.pop()


if is_remaining_bottles:
    print(f"Bottles: {' '.join(map(str,bottles))}")
if is_remaining_cups:
    print(f"Cups: {' '.join(map(str,cups))}")

print(f"Wasted litters of water: {wasted_water}")

