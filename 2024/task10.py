import numpy as np


def part1(lines):
    content = list(map(lambda x: [int(y) for y in x.strip('\n')], lines))
    array = np.array(content)

    results = set()

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] != 0: continue

            check_point(array, i, j, i, j, results)

    print(len(results))
            

def check_point(array, x, y, sx,sy, results):
    curr_height = array[x][y]
    expect_height = curr_height + 1

    if curr_height == 9:
        results.add((sx, sy, x, y))
        return

    if x + 1 < len(array) and array[x + 1][y] == expect_height:
        check_point(array, x+1, y, sx, sy, results)

    if y + 1 < len(array[0]) and array[x][y + 1] == expect_height:
        check_point(array, x, y+1, sx,sy, results)

    if x-1 >= 0 and array[x - 1][y] == expect_height:
        check_point(array, x-1, y, sx, sy, results)

    if y-1 >= 0 and array[x][y - 1] == expect_height:
        check_point(array, x, y-1, sx, sy, results)
    


import numpy as np


def part2(lines):
    content = list(map(lambda x: [int(y) for y in x.strip('\n')], lines))
    array = np.array(content)

    counter = 0

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] != 0: continue

            counter += check_point2(array, i, j, 0)
    
    print(counter)

            

def check_point2(array, x, y, results):
    curr_height = array[x][y]
    expect_height = curr_height + 1

    if curr_height == 9:
        return results + 1

    if x + 1 < len(array) and array[x + 1][y] == expect_height:
        results = check_point2(array, x+1, y, results)

    if y + 1 < len(array[0]) and array[x][y + 1] == expect_height:
        results =check_point2(array, x, y+1, results)

    if x-1 >= 0 and array[x - 1][y] == expect_height:
        results =check_point2(array, x-1, y, results)

    if y-1 >= 0 and array[x][y - 1] == expect_height:
        results = check_point2(array, x, y-1, results)

    return results
    