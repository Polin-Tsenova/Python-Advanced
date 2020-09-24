parentheses = input()
stack = []
pairs = {
    '(' : ')',
    '[' : ']',
    '{' : '}'
}
valid = True

for i in parentheses:
    if i in '({[':
        stack.append(i)
    elif i in ')}]':
        if stack:
            current = stack[-1]
            if pairs[current] == i:
                stack.pop()
            else:
                valid = False
                break
        else:
            valid = False
            break

if valid:
    print('YES')
else:
    print('NO')

