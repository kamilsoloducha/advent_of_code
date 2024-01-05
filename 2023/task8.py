import re


def task8_2(lines):
    moves = lines[0].replace("\n", '')
    print(len(moves))

    moves_map = {}

    for line in lines[2:]:
        match_el = re.findall("[A-Z0-9]+", line)
        if match_el[0] in moves_map:
            print("!!!!!!!!!!!!!!!!!!!")
        moves_map[match_el[0]] = match_el[1:3]

    beginnings = []

    for key in moves_map.keys():
        if key[2] == "A":
            beginnings.append(key)

    print(beginnings)

    # ['MLA' 19241, 'BQA' 18157, 'MJA' 19783, 'AAA' 16531, 'TGA' 21409, 'BJA' 14363]
    24035773251517
    is_found = False
    step = beginnings[5]
    counter = 0

    while not is_found:
        for move in moves:
            counter += 1
            decision = moves_map[step]
            if move == "L":
                step = decision[0]
            else:
                step = decision[1]

            if step[2] == "Z":
                print(counter)
                counter = 0



def task_8_1(lines):
    moves = lines[0].replace("\n", '')
    print(len(moves))

    moves_map = {}

    for line in lines[2:]:
        match_el = re.findall("[A-Z]+", line)
        if match_el[0] in moves_map:
            print("!!!!!!!!!!!!!!!!!!!")
        moves_map[match_el[0]] = match_el[1:3]

    counter = 0
    is_found = False
    step = 'AAA'

    while not is_found:
        for move in moves:
            counter += 1
            decision = moves_map[step]
            if move == "L":
                step = decision[0]
            else:
                step = decision[1]

            if step == "ZZZ":
                is_found = True
                break

            if counter % 100000 == 0:
                print(counter)

    print(counter)
