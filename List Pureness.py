from collections import deque

def best_list_pureness(numbers, rot):
    nums = deque(numbers)
    results = {}
    res = ''

    for i in range(0, rot+1):
        pureness = 0
        for el in nums:
            pureness += el * nums.index(el)
        results[i] = pureness
        nums.appendleft(nums.pop())

    all_values = results.values()
    max_value = max(all_values)

    for k, v in results.items():
        if v == max_value:
            res = f"Best pureness {v} after {k} rotations"
            break
    return res



test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

