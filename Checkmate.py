matrix = []

def is_valid(r, c, matrix):
    n = len(matrix)
    return 0 <= r < n and 0 <= c < n

for _ in range(8):
    line = [x for x in input().split()]
    matrix.append(line)

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

queen_positions = []
for r in range(8):
    for c in range(8):
        if matrix[r][c] == 'Q':
            queen_positions.append([r, c])

for queen in queen_positions:
    queen_row = queen[0]
    queen_col = queen[1]
    for direction in directions:
        change = directions[direction]
        change_row = change[0]
        change_col = change[1]
        new_pos = [queen_row + change_row, queen_col + change_col]
        new_row = new_pos[0]
        new_col = new_pos[1]
        while is_valid(new_row, new_col, matrix):
            if matrix[new_row][new_col] == '.':
                new_row += directions[direction][0]
                new_col += directions[direction][1]
            if matrix[new_row][new_col] == 'Q':
                break
            if matrix[new_row][new_col] == ' K':
                print(queen)
                continue
        else:
            continue