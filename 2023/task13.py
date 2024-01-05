from collections import defaultdict
import numpy as np


def task1(lines):
    maps = []
    current_map = []
    maps.append(current_map)

    for line in lines:
        if line == '\n':
            current_map = []
            maps.append(current_map)
        else:
            current_map.append(line.replace("\n", ""))

    counter = 0

    for item in maps:
        symetry_lines = find_symetry_lines(item[0])
        for line in item:
            symetry_lines = find_symetry_lines(line) & symetry_lines
            if len(symetry_lines) == 0:
                break

        if len(symetry_lines) == 1:
            counter += symetry_lines.pop()
            continue

        column = get_column(item, 0)
        symetry_lines = find_symetry_lines(column)
        for i in range(len(item[0])):
            column = get_column(item, i)
            symetry_lines = find_symetry_lines(column) & symetry_lines
            if len(symetry_lines) == 1:
                break

        if len(symetry_lines) == 0:
            print("!!!!!!!!!!!error!!!!!!!!!!")
        counter += symetry_lines.pop() * 100

    print(counter)
    return


def task2(lines):
    maps = []
    current_map = []
    maps.append(current_map)

    for line in lines:
        if line == '\n':
            current_map = []
            maps.append(current_map)
        else:
            current_map.append([*line.replace("\n", "")])

    counter = 0

    for item in maps:
        counter += (find_symetry_line(item) + 1)
        counter += ((find_symetry_line(np.array(item).transpose()) + 1) * 100)

    print(counter)


        # for i in range(len(item)):
            # new_symetry_lines = find_new_symetry_lines(item[i])
            # new_symetry_lines = filter_chances(new_symetry_lines, old_symetries, i)
            # old_symetry_lines = find_old_symetry_lines(item[i])

            # print(i)
            # print(new_symetry_lines)
            # print(old_symetries)
            # print()


    #         symetry_lines = find_symetry_lines(line) & symetry_lines
    #         if len(symetry_lines) == 0:
    #             break

    #     symetry_lines = find_symetry_lines(item[0])
    #     for line in item:
    #         symetry_lines = find_symetry_lines(line) & symetry_lines
    #         if len(symetry_lines) == 0:
    #             break
    #
    #     if len(symetry_lines) == 1:
    #         counter += symetry_lines.pop()
    #         continue
    #
    #     column = get_column(item, 0)
    #     symetry_lines = find_symetry_lines(column)
    #     for i in range(len(item[0])):
    #         column = get_column(item, i)
    #         symetry_lines = find_symetry_lines(column) & symetry_lines
    #         if len(symetry_lines) == 1:
    #             break
    #
    #     if len(symetry_lines) == 0:
    #         print("!!!!!!!!!!!error!!!!!!!!!!")
    #     counter += symetry_lines.pop() * 100
    #
    # print(counter)
    return


def find_symetry_line(item):
    old_symetries = []

    # Find all chances for symetry for all rows
    for i in range(len(item)):
        old_symetries.append(find_old_symetry_lines(item[i]))

    # print(old_symetries)

    # Find old symetry line
    old_symetry = set(old_symetries[0])
    for old_symetry_item in old_symetries:
        old_symetry = set(old_symetry) & set(old_symetry_item)

    # print(old_symetry)

    # find merge all chances
    new_chances = set(old_symetries[0])
    for old_symetry_item in old_symetries:
        new_chances = set(new_chances) | set(old_symetry_item)

    # exclude old symetry line
    new_chances = new_chances.difference(old_symetry)
    # print(new_chances)

    missing_map = {}
    # for all chances
    # in all old symetry lines
    # check where new chance not exists and store it in missing_map
    for new_chance in new_chances:
        for old_symetry_item in old_symetries:
            if new_chance not in old_symetry_item:
                if new_chance in missing_map:
                    missing_map[new_chance] += 1
                else:
                    missing_map[new_chance] = 1
    # print('missing_map', missing_map)
    # missing_map contains pairs where is the chance for symetry line at KEY column
    # and how many times VALUE column can be symetry line

    for missing_item in missing_map:
        value = missing_map[missing_item]
        # should ignore when value is more than 1
        # because we can change just 1 pixel
        if value != 1:
            continue

        return missing_item
    return -1


def find_new_symetry_lines(line):
    line = line.copy()
    result = []
    for i in range(len(line)):
        change(line, i)
        for j in range(len(line) - 1):
            if line[j] == line[j + 1] and check_symetry_line(line, j):
                result.append(Chance(j, i))
        change(line, i)

    return result


def filter_chances(chances, old_symetries, index):
    result = []
    for chance in chances:
        for i, old_array in enumerate(old_symetries):
            if i == index:
                continue






def find_old_symetry_lines(line):
    result = []
    for i in range(len(line)-1):
        if line[i] == line[i+1] and check_symetry_line(line, i):
            result.append(i)
    return result


def get_column(table, index):
    column = []
    for line in table:
        column.append(line[index])
    return column


def find_symetry_lines(line):
    result = []
    for i in range(len(line)-1):
        if line[i] == line[i+1] and check_symetry_line(line, i):
            result.append(i+1)
    return set(result)


def check_symetry_line(line, i):
    for j in range(len(line) - i):
        if (i-j >= 0 and i+1+j < len(line)) and line[i-j] != line[i+1+j]:
            return False
    return True

def change(array, index):
    if array[index] == '.':
        array[index] = '#'
    else:
        array[index] = '.'

def merge_sets(set1, set2):
    result_set = {}



    return set2


class Chance:
    id = -1
    index_to_change = -1

    def __init__(self, _id, index_to_change):
        self.id = _id
        self.index_to_change = index_to_change

    def __str__(self):
        return f'[{self.id} - {self.index_to_change}]'

    def __repr__(self):
        return str(self)
