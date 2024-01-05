import util
import re


def task_3_1(lines):
    table = util.to_2_dim_array(lines)
    hot_points = find_hot_points(table)
    sum = 0
    y = 0
    for line in lines:
        x = 0
        numbers = re.findall('[0-9]+', line)

        for number in numbers:
            number_beginning = line.find(number, x)
            is_used = False

            for index in range(number_beginning, number_beginning + len(number)):
                x = index

                if is_used or any(point.x == index and point.y == y for point in hot_points):
                    is_used = True

                if is_used:
                    break

            if is_used:
                print(number + " add")
                sum += int(number)
            else:
                print(number + " skip")

        y += 1

    print(sum)


def task_3_2(lines):
    table = util.to_2_dim_array(lines)
    gears = find_gears(table)
    sum = 0

    for gear in gears:
        important_lines = find_lines(gear, lines)
        numbers = find_numbers_around(gear, important_lines)
        if len(numbers) > 1:
            ratio = 1
            for number in numbers:
                ratio *= number
            sum += ratio

    print(sum)


def find_gears(table):
    gear_points = []
    for i in range(len(table)):
        for j in range(len(table[i])):
            char = table[i][j]
            if char == '*':
                gear_points.append(util.Point(j, i))
    return gear_points


def find_lines(point, lines):
    important_lines = []

    ids = range(point.y - 1, point.y + 2)
    ids = filter(lambda x: 0 <= x < len(lines), ids)

    for id in ids:
        important_lines.append(lines[id])

    return important_lines


def find_numbers_around(point, lines):
    found_numbers = []

    for line in lines:
        x = 0
        numbers = re.findall('[0-9]+', line)

        for number in numbers:
            beginning = line.find(number, x)
            end = beginning + len(number) - 1
            x = end

            if (beginning < point.x - 1 and end < point.x - 1) or (beginning > point.x + 1 and end > point.x + 1):
                continue

            found_numbers.append(int(number))

    return found_numbers



def task_3_1v1(lines):
    table = util.to_2_dim_array(lines)
    numbers = []
    index = 0

    for line in lines:
        temp_numbers = find_numbers(line, index)
        numbers += temp_numbers
        index += 1

    hot_points = find_hot_points(table)

    for number in numbers:
        for point in number.points:
            if any(point == x for x in hot_points):
                number.is_used = True
                break

        if number.is_used:
            continue

    print(numbers)

    filtered = filter(lambda x: x.is_used, numbers)

    sum = 0
    for number in filtered:
        sum += number.value

    print(sum)
    return None


def find_numbers(line, line_index):
    result = []
    numbers = re.findall('[0-9]+', line)
    print(numbers)
    index = 0
    for number in numbers:
        index = line.find(number, index)
        points = []

        for i in range(index, index + len(number)+1):
            points.append(util.Point(line_index, i))

        result.append(Number(int(number), points))
        index+=1

    return result


def find_hot_points(table):
    points = []
    for i in range(len(table)):
        for j in range(len(table[i])):
            char = table[i][j]
            if char.isnumeric() or char == '.' or char == '\n':
                continue
            points_around = find_around(i, j)
            for point in points_around:
                points.append(point)

    return points


def find_around(x, y):
    points = []
    for i in range(x - 1, x + 2):
        if i < 0:
            continue
        for j in range(y - 1, y + 2):
            if j < 0:
                continue

            points.append(util.Point(j, i))
    return points


class Number:
    value = 0
    points = []
    is_used = False

    def __init__(self, value, points):
        self.value = value
        self.points = points

    def print(self):
        print(self.value, self.is_used, self.points)


class Gear:
    point = None
    points_around = []
    numbers = []

    def __init__(self, point):
        self.point = point
        self.points_around = find_around(point.x, point.y)