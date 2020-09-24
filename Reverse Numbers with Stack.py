stack = input().split()
new_stack = []
while len(stack) > 0:
    new_stack.append(stack.pop())
print(" ".join(new_stack))
