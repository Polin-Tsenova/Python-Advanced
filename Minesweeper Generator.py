import re


def is_valid(row, col, matrix):
    n = len(matrix)
    return 0 <= row < n and 0 <= col < n


n = int(input())
bombs = int(input())

directions = {
    'up':[-1,0],
    'down': [1, 0],
    'right':[0, 1],
    'left': [0, -1],
    'upleft':[-1, -1],
    'upright':[-1, 1],
    'downleft':[1, -1],
    'downright':[1, 1]
}

matrix = [['0' for _ in range(n)] for _ in range(n)]

for i in range(bombs):
    # bomb_pos = (input().split(', '))
    # r = int(bomb_pos[0][1])
    # c = int(bomb_pos[1][0])
    bomb_pos = [int(x) for x in re.findall(r'-?\d+', input())]
    if bomb_pos:
        r = bomb_pos[0]
        c = bomb_pos[1]
    if is_valid(r, c,matrix):
        matrix[r][c] = '*'

for r in range(n):
    for c in range(n):
        if matrix[r][c] == '*':
            for direction in directions:
                change = directions[direction]
                new_r = r + change[0]
                new_c = c + change[1]
                if is_valid(new_r, new_c, matrix):
                    if matrix[new_r][new_c] == '*':
                        continue
                    matrix[new_r][new_c] = str(int(matrix[new_r][new_c]) + 1)

[print(' '.join(row)) for row in matrix]
