from collections import deque


def solve(people, n):
    people = deque(people)
    index = 0
    while people:
        person = people.popleft()
        index += 1
        if index == n:
            index = 0
            if people:
                print(f"Removed {person}")
            else:
                print(f"Last in {person}")
        else:
            people.append(person)


people = input().split()
num = int(input())
solve(people, num)

# Test Input
# George Peter Michael William Thomas
# 10