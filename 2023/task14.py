import time

import util
import numpy as np


def task1(lines):
    lines = map(lambda x: x.replace('\n', ''), lines)
    table = util.to_2_dim_array(lines)
    load = 0
    max_value = len(table)
    print("max_value", max_value)

    for column_x in range(len(table[0])):

        beginning = -1
        stones = 0
        column_load = 0
        for row_y in range(len(table)):
            pixel = table[row_y][column_x]
            if beginning < 0 and pixel in ['.', 'O']:
                beginning = max_value - row_y

            if pixel == '.':
                continue

            if pixel == 'O':
                stones += 1
                continue

            if pixel == '#':
                for i in range(stones):
                    column_load += beginning
                    beginning -= 1

                stones = 0
                beginning = -1

        for i in range(stones):
            column_load += beginning
            beginning -= 1

        print(column_load)
        load += column_load

    print(load)
    return


def task2(lines):
    lines = map(lambda x: x.replace('\n', ''), lines)
    table = util.to_2_dim_array(lines)
    table = np.array(table)
    for j in range(1000):
        for i in range(4):
            move_north(table)
            table = np.rot90(table, -1)

        if j % 1_00 == 0:
            print(j)

    print(table)

    sum = 0
    counter = len(table)
    for row in table:
        for char in row:
            if char == 'O':
                sum += counter
        counter -= 1

    print(sum)

    return


def move_north(table):
    for i in range(table.shape[1]):
        column = table[:, i]
        move_line(column)


def move_line(line):
    stones = []
    for row_y in range(len(line) - 1, -1, -1):
        pixel = line[row_y]
        if pixel == 'O':
            stones.append(row_y)
            continue

        if pixel == '#' and len(stones) > 0:
            for stone in stones:
                line[stone] = '.'

            for i in range(row_y + 1, row_y + len(stones) + 1):
                line[i] = 'O'

            stones = []

    for stone in stones:
        line[stone] = '.'

    for i in range(0, len(stones)):
        line[i] = 'O'
