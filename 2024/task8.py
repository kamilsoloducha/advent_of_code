import numpy as np


def part1(lines):
    content = list(map(lambda x: [y for y in x.strip('\n')], lines))
    array = np.array(content)
    marker = array.copy()
    print(array)
    rows = len(array)
    cols = len(array[0])
    antinodes = set();

    for i in range(rows):
        for j in range(cols):
            if array[i][j] == '.':
                continue

            antena = array[i][j]

            for k in range(rows):
                for l in range(cols):
                    if array[k][l] != antena or (k==i and l==j): continue

                    diff_x = abs(i-k)
                    diff_y = abs(j-l)

                    x1 = 0
                    x2 = 0
                    y1= 0
                    y2= 0

                    if i<k: 
                        x1 = i-diff_x
                        x2 = k+diff_x
                    else: 
                        x2 = k-diff_x
                        x1 = i+diff_x

                    if j<l: 
                        y1 = j-diff_y
                        y2 = l+diff_y
                    else: 
                        y2 = l-diff_y
                        y1 = j+diff_y

                    if x1 >= 0 and x1 < rows and y1 >=0 and y1 < cols:
                        antinodes.add((x1, y1))
                        marker[x1][y1] = '#'
                        # print(marker)

                    if x2 >= 0 and x2 < rows and y2 >=0 and y2 < cols:
                        antinodes.add((x2, y2))
                        marker[x2][y2] = '#'
                        # print(marker)


    print(len(antinodes))
    print(marker)

import numpy as np


def part2(lines):
    content = list(map(lambda x: [y for y in x.strip('\n')], lines))
    array = np.array(content)
    marker = array.copy()
    print(array)
    rows = len(array)
    cols = len(array[0])
    antinodes = set();

    for i in range(rows):
        for j in range(cols):
            if array[i][j] == '.':
                continue

            antena = array[i][j]

            for k in range(rows):
                for l in range(cols):
                    if array[k][l] != antena or (k==i and l==j): continue
                    antinodes.add((i, j))
                    counter = 1
                    keep_going = 1
                    while keep_going > 0:
                        keep_going = 0
                        diff_x = abs(i-k)
                        diff_y = abs(j-l)

                        x1 = 0
                        x2 = 0
                        y1= 0
                        y2= 0

                        if i<k: 
                            x1 = i-diff_x*counter
                            x2 = k+diff_x*counter
                        else: 
                            x2 = k-diff_x*counter
                            x1 = i+diff_x*counter

                        if j<l: 
                            y1 = j-diff_y*counter
                            y2 = l+diff_y*counter
                        else: 
                            y2 = l-diff_y*counter
                            y1 = j+diff_y*counter

                        if x1 >= 0 and x1 < rows and y1 >=0 and y1 < cols:
                            antinodes.add((x1, y1))
                            marker[x1][y1] = '#'
                            print(marker)
                            keep_going += 1

                        if x2 >= 0 and x2 < rows and y2 >=0 and y2 < cols:
                            antinodes.add((x2, y2))
                            marker[x2][y2] = '#'
                            print(marker)
                            keep_going += 1
                        counter += 1


    print(len(antinodes))
    print(marker)

    
    