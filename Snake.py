def is_valid(row, col, matrix):
    n = len(matrix)
    return 0 <= row < n and 0 <= col < n


n = int(input())
matrix = [[i for el in input().split() for i in el] for _ in range(n)]

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

start_pos = []
food = 0
is_out = False

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == 'S':
            start_pos = [row_index, col_index]


while True:
    command = input()
    dir = directions[command]
    new_pos = [start_pos[0]+ dir[0], start_pos[1] + dir[1]]
    r = new_pos[0]
    c = new_pos[1]

    if is_valid(r, c, matrix):
        if matrix[r][c] == '*':
            food += 1
            matrix[start_pos[0]][start_pos[1]] = '.'
            matrix[r][c] = 'S'
            start_pos = new_pos
        if matrix[r][c] == 'B':
            for row_index in range(len(matrix)):
                for col_index in range(len(matrix[row_index])):
                    if matrix[row_index][col_index] == 'B' and row_index!= r and col_index != c:
                        matrix[start_pos[0]][start_pos[1]] = '.'
                        matrix[r][c] = '.'
                        matrix[row_index][col_index] = '.'
                        start_pos = [row_index, col_index]
        if matrix[r][c] == '-':
            matrix[start_pos[0]][start_pos[1]] = '.'
            matrix[r][c] = 'S'
            start_pos = new_pos
    else:
        matrix[start_pos[0]][start_pos[1]] = '.'
        print("Game over!")
        break

    if food >= 10:
        print("You won! You fed the snake.")
        break

print(f"Food eaten: {food}")
[print(''.join(row)) for row in matrix]
