def solve(str):
    s = []
    for ch in str:
        s.append(ch)

    reverse_str = ''

    while s:
        reverse_str += s.pop()

    return reverse_str


print(solve(input()))
