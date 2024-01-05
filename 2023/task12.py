def task1(lines):
    maps = []
    numbers = []

    for line in lines:
        elements = line.replace('\n', '').split(" ")
        maps.append(elements[0])
        numbers.append(list(map(int, elements[1].split(','))))

    counter = 0

    for i in range(len(maps)):
        print(maps[i], numbers[i])

        considering = ['.'] * len(maps[i])
        counter += put_next_and_check(maps[i], numbers[i], considering)

    print(counter)

def task2(lines):
    maps = []
    numbers = []

    for line in lines:
        elements = line.replace('\n', '').split(" ")
        maps.append(elements[0])
        numbers.append(list(map(int, elements[1].split(','))))

    counter = 0

    for i in range(len(maps)):
        # print(maps[i], numbers[i])

        new_map = get_new_map(maps[i])
        new_numbers = numbers[i]*5
        # print(new_map, new_numbers)

        considering = ['.'] * len(new_map)
        counter += put_next_and_check(new_map, new_numbers, considering)

    print(counter)


def get_new_map(current):
    new_map = []
    for i in range(0, 6):
        for j in range(0, len(current)):
            new_map.append(current[j])
        if i != 5:
            new_map.append('?')
    return new_map


def put_next_and_check(springs, numbers, considering):
    last = last_marked(considering) + 1
    first = 0
    if last != 0:
        first = last + 1

    counter = 0

    current_number = numbers[0]
    copy_numbers = numbers[1:]

    for i in range(first, len(springs)):

        copy_considering = considering.copy()

        if i + current_number > len(springs):
            return counter

        for j in range(i, i+current_number):
            copy_considering[j] = '#'

        if len(copy_numbers) == 0:
            if compare(copy_considering, springs):
                counter += 1
        else:
            counter += put_next_and_check(springs, copy_numbers, copy_considering)

    return counter


def compare(considering, original):
    if len(considering) != len(original):
        print('ERROR!!!!!!!!')
        raise Exception(considering, original)

    for i in range(len(considering)):
        if (original[i] == '.' and considering[i] == '#') or (considering[i] == '.' and original[i] == '#'):
            return False
    return True


def last_marked(considering):
    for i in range(len(considering) - 1, -1, -1):
        if considering[i] == '#':
            return i
    return -1
