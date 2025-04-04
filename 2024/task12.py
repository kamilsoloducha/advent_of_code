import numpy as np
import functools

def part1(lines):
    content = list(map(lambda x: [y for y in x.strip('\n')], lines))
    array = np.array(content)
    print(array)

    visited = set();
    counter = 0

    for i in range(len(array)):
        for j in range(len(array[i])):
            if (i, j) in visited: continue

            new_area = find_area(array, i, j)

            for item in new_area:
                visited.add((item))
            
            perimeter = 0

            for item in new_area:
                perimeter += get_perimeter(array, item[0], item[1])

            counter += len(new_area) * perimeter
    
    print('Counter: ', counter)
            

def find_area(array, i, j):
    new_area = set()
    size = 0
    new_area.add((i, j))

    while size != len(new_area):
        size = len(new_area)
        new_area_list = list(new_area)
        for k in range(size):
            x = new_area_list[k][0]
            y = new_area_list[k][1]

            if x > 0 and array[x][y] == array[x-1][y]:
                new_area.add((x-1, y))
            if y > 0 and array[x][y] == array[x][y-1]:
                new_area.add((x, y-1))
            if x < len(array) -1 and array[x][y] == array[x+1][y]:
                new_area.add((x+1, y))
            if y < len(array[0]) -1 and array[x][y] == array[x][y+1]:
                new_area.add((x, y+1))

    return new_area


def get_perimeter(array, i, j):
    counter = 0
    if i == 0 or array[i][j] != array[i-1][j]:
        counter += 1
    if j == 0 or array[i][j] != array[i][j-1]:
        counter += 1
    if i == len(array) - 1 or array[i][j] != array[i+1][j]:
        counter += 1
    if j == len(array[0]) - 1 or array[i][j] != array[i][j+1]:
        counter += 1

    return counter
    
def part2(lines):
    content = list(map(lambda x: [y for y in x.strip('\n')], lines))
    array = np.array(content)
    print(array)

    visited = set();
    counter = 0

    for i in range(len(array)):
        for j in range(len(array[i])):
            if (i, j) in visited: continue

            new_area = find_area(array, i, j)

            for item in new_area:
                visited.add((item))
            
            
            new_area = set(sorted(list(new_area), key=functools.cmp_to_key(compare)))
            perimeter = 0

            counter += len(new_area) * perimeter
    
    print('Counter: ', counter)

def get_only_perimeter(array, area):
    perimeter = set()
    for item in area:
        x = item[0]
        y = item[1]

        if x == 0 or y == 0 or x == len(array) - 1 or y == len(array[0]) - 1:
            perimeter.add((x, y))
            continue
        
        curr = array[x][y]
        if curr != array[x-1][y] or curr != array[x][y-1] or curr != array[x+1][y] or curr != array[x][y+1]:
            perimeter.add((x, y))

    return perimeter

def compare(item1, item2):
    if item1[0] == item2[0]:
        return item1[1] - item2[1]
    else: 
        return item1[0] - item2[0]