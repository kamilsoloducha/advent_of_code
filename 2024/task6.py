import numpy as np

dirs = ['^','>','v','<']
moves = {
    '^': [-1, 0],
    '>': [0, 1],
    'v': [1, 0],
    '<': [0, -1],
}

def part1(lines):
    content = list(map(lambda x: [y for y in x.strip('\n')], lines))
    array = np.array(content)

    pos = [0,0]
    start_dir = '^'

    for i in range(len(array)):
        for j in range(len(array[i])):

            if array[i][j] == start_dir:
                pos[0] = i
                pos[1] = j

    while not is_outside(array, get_next_pos(array, pos)):
        if is_obstacle(array, pos):
            change_dir(array, pos)
        else:
            pos = move(array, pos)
        print(array)
    array[pos[0]][pos[1]] = 'X'
    print(count(array))

def count(array):
    counter = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 'X':
                counter += 1

    return counter

def change_dir(array, pos):
    array[pos[0]][pos[1]] = get_next_direction(array, pos)

def get_current_dir(array, pos):
    return array[pos[0]][pos[1]]

def get_next_direction(array, pos):
    dir = get_current_dir(array, pos)
    next_dir_id = dirs.index(dir) + 1
    if next_dir_id > 3:
        return dirs[0]
    else:
        return dirs[next_dir_id]

def is_obstacle(array, pos):
    next_pos = get_next_pos(array, pos)
    return array[next_pos[0]][next_pos[1]] == '#'

def get_next_pos(array, pos):
    dir = get_current_dir(array, pos)
    next_move = moves[dir]
    next_x = pos[0] + next_move[0]
    next_y = pos[1] + next_move[1]
    return [next_x, next_y]

def move(array, pos):
    next_pos = get_next_pos(array, pos)
    array[next_pos[0]][next_pos[1]] = array[pos[0]][pos[1]]
    array[pos[0]][pos[1]] = 'X'
    return next_pos

def is_outside(array, pos):
    return pos[0] < 0 or pos[0] > len(array) -1 or pos[1] < 0 or pos[1] > len(array[1]) - 1


def part2(lines):
    content = list(map(lambda x: [y for y in x.strip('\n')], lines))
    array = np.array(content)

    pos = [0,0]
    start_dir = '^'

    for i in range(len(array)):
        for j in range(len(array[i])):

            if array[i][j] == start_dir:
                pos[0] = i
                pos[1] = j
    original_start = pos
    original_map = array.copy()

    counter = 0

    for i in range(len(array)):
        for j in range(len(array[i])):

            if original_map[i][j] != '.':
                continue

            array = original_map.copy()
            array[i][j] = '#'

            if in_the_loop(array, original_start):
                counter += 1

    print(counter)


def in_the_loop(array, pos):
    history = set()
    while not is_outside(array, get_next_pos(array, pos)):
        history.add((pos[0],pos[1], get_current_dir(array, pos)))
        if is_obstacle(array, pos):
            change_dir(array, pos)
        else:
            pos = move(array, pos)
            if (pos[0],pos[1], get_current_dir(array, pos)) in history:
                return True

    return False

def hit_same_field(history, array, pos):
    for item in history:
        if item[0] == pos and item[1] == get_current_dir(array, pos):
            return True
    return False

def dist_history(history):
    new_history = []
    for item in history:
        exists = False

        for x in new_history:

            exists = item[0][0] == x[0][0] and item[0][1] == x[0][1] and item[1] == x[1]

        if not exists:
            new_history.append(item)

    return new_history