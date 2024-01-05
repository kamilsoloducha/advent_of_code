import sys
import time
import queue

import numpy as np
import util as u


def task1(content):
    content = list(map(lambda x: [int(y) for y in x.strip('\n')], content))
    array = np.array(content)
    marker = array.copy()

    end_x = array.shape[1]
    end_y = array.shape[0]

    for y in range(end_y):
        for x in range(end_x):
            marker[y][x] = sys.maxsize

    beams = [Beam(u.Point(0, 0), u.Point(1, 0), 0, 1)]

    while len(beams) > 0:
        current_beam = beams.pop(len(beams) - 1)
        current_value = current_beam.sum
        increase = array[current_beam.position.y][current_beam.position.x]
        current_value = current_value + increase
        if marker[current_beam.position.y][current_beam.position.x] <= current_value:
            continue

        marker[current_beam.position.y][current_beam.position.x] = current_value
        current_beam.sum = current_value

        new_beams = get_next(current_beam, end_x, end_y)
        for beam in new_beams:
            beams.append(beam)

    print(marker[end_y-1][end_x-1])
    print(marker)

def get_next(beam: 'Beam', max_x, max_y):
    beams = []
    beam.counter += 1

    if not beam.counter > 3:
        new_x = beam.position.x + beam.direction.x
        new_y = beam.position.y + beam.direction.y

        if not (new_x < 0 or new_y < 0 or new_x >= max_x or new_y >= max_y):
            beams.append(Beam(u.Point(new_x, new_y), beam.direction, beam.sum, beam.counter, beam.path.copy()))

    for multiplier in [1, -1]:
        new_direction = u.Point(beam.direction.y * multiplier, beam.direction.x * multiplier)

        new_x = beam.position.x + new_direction.x
        new_y = beam.position.y + new_direction.y

        if not (new_x < 0 or new_y < 0 or new_x >= max_x or new_y >= max_y):
            beams.append(Beam(u.Point(new_x, new_y), new_direction, beam.sum, 0, beam.path.copy()))

    return beams


class Beam:
    path = []
    position: u.Point = None
    direction: u.Point = None
    sum = 0
    counter = 0

    def __init__(self, position, direction, sum=0, counter=0, path=None):
        if path is None:
            path = []
        path.append(position)
        self.path = path
        self.position = position
        self.direction = direction
        self.sum = sum
        self.counter = counter


    def __str__(self):
        return f'[pos:{self.position}, dir:{self.direction}]'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.position == other.position and self.direction == other.direction
