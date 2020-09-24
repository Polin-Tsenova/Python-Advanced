from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence_value = int(input())
bullets_count = 0
is_defeated = False

while True:
    if not locks:
        break
    if not bullets:
        is_defeated = True
        break
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    bullets_count += 1
    if current_bullet > current_lock:
        print("Ping!")
        locks.appendleft(current_lock)
    elif current_bullet <= current_lock:
        print("Bang!")
    if bullets_count % barrel_size == 0 and bullets:
        print('Reloading!')
        # barrel_size *= 2


bullets_cost = bullets_count * bullet_price
earned = intelligence_value - bullets_cost

if is_defeated:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${earned}")


