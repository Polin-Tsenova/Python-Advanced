numbers = [int(x) for x in input().split()]
to_push, to_pop, searched_number = numbers

stack = [int(x) for x in input().split()][:to_push]

#The same as the following below it
# for _ in range(to_pop):
#     stack.pop()
[stack.pop() for _ in range(to_pop)]

if searched_number in stack:
    print("True")
else:
    if stack:
        print(min(stack))
    else:
        print('0')

# Test input
# 5 2 13
# 1 13 45 32 4

# 3 3 90
# 90 90 90