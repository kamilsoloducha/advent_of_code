import time

import numpy as np
import util


def task1(content):
    print(calculate(content, Beam(util.Point(0, 0), util.Point(1, 0))))


def task2(content):
    lines = map(lambda x: x.replace('\n', ''), content)
    table1 = util.to_2_dim_array(lines)
    max_x = len(table1[0])
    max_y = len(table1)

    max_sum = 0

    for x in range(max_x):
        beginning_beam = Beam(util.Point(x, 0), util.Point(0, 1))
        sum = calculate(content, beginning_beam)
        if max_sum < sum:
            max_sum = sum

        beginning_beam = Beam(util.Point(x, max_y - 1), util.Point(0, -1))
        sum = calculate(content, beginning_beam)
        if max_sum < sum:
            max_sum = sum

    for y in range(max_y):
        beginning_beam = Beam(util.Point(0, y), util.Point(1, 0))
        sum = calculate(content, beginning_beam)
        if max_sum < sum:
            max_sum = sum

        beginning_beam = Beam(util.Point(max_x - 1, y), util.Point(-1, 0))
        sum = calculate(content, beginning_beam)
        if max_sum < sum:
            max_sum = sum

    print(max_sum)

def calculate(content, beginning_beam):
    lines = map(lambda x: x.replace('\n', ''), content)
    table1 = util.to_2_dim_array(lines)
    table = np.array(table1)
    max_x = len(table[0])
    max_y = len(table)
    tracking = {}

    remaining_beams = [beginning_beam]

    while len(remaining_beams) > 0:
        current_beam = remaining_beams.pop(0)
        current_sign = table[current_beam.position.y][current_beam.position.x]
        current_dir = current_beam.direction

        if current_beam.position in tracking:
            if any(direction == current_dir for direction in tracking[current_beam.position]):
                continue
            else:
                tracking[current_beam.position].append(current_dir)
        else:
            tracking[current_beam.position] = [current_dir]

        next_directions = get_next(current_dir, current_sign)
        for direction in next_directions:
            next_position = util.Point(current_beam.position.x + direction.x, current_beam.position.y + direction.y)
            if next_position.x < 0 or next_position.x >= max_x or next_position.y < 0 or next_position.y >= max_y:
                continue
            remaining_beams.append(Beam(next_position, direction))

        # animate(tracking, max_x, max_y)

    return len(tracking)


def animate(tracking, max_x, max_y):
    for y in range(max_y):
        for x in range(max_x):
            if util.Point(x, y) in tracking:
                sign = '#'
            else:
                sign = '.'
            print(sign, end='')
        print("\n", end='')

    time.sleep(0.3)


def get_next(direction: util.Point, sign: str):
    match sign:
        case '.':
            return [direction]
        case '-':
            if direction.y == 0:
                return [direction]
            else:
                return [util.Point(1, 0), util.Point(-1, 0)]
        case '|':
            if direction.x == 0:
                return [direction]
            else:
                return [util.Point(0, 1), util.Point(0, -1)]
        case '/':
            return [util.Point(direction.y * (-1), direction.x * (-1))]
        case '\\':
            return [util.Point(direction.y, direction.x)]


class Beam:
    position: util.Point = None
    direction: util.Point = None

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def __str__(self):
        return f'[pos:{self.position}, dir:{self.direction}]'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.position == other.position and self.direction == other.direction
