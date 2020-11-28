def is_valid(m, row, col):
    size = len(m)
    return 0 <= row < size and 0 <= col < size and m[row][col] > 0


def detronate(row, col, matrix):
    bomb_value = matrix[row][col]
    if bomb_value > 0:
        for current_row in range(-1, 2):
            for current_col in range(-1, 2):
                neighbor_row = row + current_row
                neighbor_col = col + current_col
                if is_valid(matrix, neighbor_row, neighbor_col):
                    matrix[neighbor_row][neighbor_col] -= bomb_value


size = int(input())
matrix = []

for _ in range(size):
    line = [int(x) for x in input().split()]
    matrix.append(line)

positions = input().split()

for position in positions:
    position.split(',')
    r = int(position[0])
    c = int(position[2])
    for row in range(size):
        for col in range(size):
            if row == r and col == c:
                detronate(row, col, matrix)

alive_cells_count = 0
alive_cells_sum = 0

for row_index in range(size):
    for col_index in range(size):
        if matrix[row_index][col_index] > 0:
            alive_cells_count += 1
            alive_cells_sum += matrix[row_index][col_index]

print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {alive_cells_sum}")
[print(' '.join(map(str, x))) for x in matrix]

# Test Input

# 3
# 7 8 4
# 3 1 5
# 6 4 9
# 0,2 1,0 2,2
#
# 4
# 8 3 2 5
# 6 4 7 9
# 9 9 3 6
# 6 8 1 2
# 1,2 2,1 2,0
