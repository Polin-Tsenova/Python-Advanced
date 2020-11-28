DIRECTIONS = {
    "up": [-1, 0],
    "down": [1, 0],
    "right": [0, 1],
    "left": [0,-1]
}


def is_valid(n, pos):
    return 0 <= pos[0] < n and 0 <= pos[1] < n


def movement(matrix, player, dir):
    position_change = DIRECTIONS[dir]
    next_position = [player["pos"][0] + position_change[0], player["pos"][1] + position_change[1]]
    if not is_valid(len(matrix), next_position):
        if next_position[1] >= len(matrix):
            next_position[1] = 0
        elif next_position[1] < 0:
            next_position[1] = len(matrix) - 1
        elif next_position[0] >= len(matrix):
            next_position[0] = 0
        elif next_position[0] < 0:
            next_position[0] = len(matrix) - 1

    if matrix[next_position[0]][next_position[1]] == "*":
        matrix[next_position[0]][next_position[1]] = player["symbol"]
        player["pos"] = next_position
    else:
        matrix[next_position[0]][next_position[1]] = "x"
        return True


size = int(input())
matrix = []
first_player_pos = []
second_player_pos = []

for i in range(size):
    line = input()
    matrix.append([r for r in line])
    if 'f' in line:
        first_player_pos = [i, line.index('f')]
    if 's' in line:
        second_player_pos = [i, line.index('s')]

first_player = {"symbol": "f", "pos": first_player_pos}
second_player = {"symbol": "s", "pos": second_player_pos}

while True:
    command = input().split()
    first_move = command[0]
    second_move = command[1]
    is_player_dead = movement(matrix, first_player, first_move)
    if is_player_dead:
        break
    is_player_dead = movement(matrix, second_player, second_move)
    if is_player_dead:
        break

[print(''.join(row)) for row in matrix]