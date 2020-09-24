stack = []
n = int(input())

for i in range(1, n+1):
    query = input().split()
    if query[0] == '1':
        element = query[1]
        stack.append(element)
    if query[0] == '2':
        if len(stack)> 0:
            stack.pop()
    if query[0] == '3':
        print(max([int(x) for x in stack]))
    if query[0] == '4':
        print(min([int(x) for x in stack]))

stack = stack[::-1]

print(", ".join(stack))