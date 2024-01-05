import re

def task_6_1(lines):
    counters = []
    times = get_numbers(lines[0])
    distances = get_numbers(lines[1])

    for i, value in enumerate(times):
        record = distances[i]
        counter = 0
        for acc_time in range(0, value + 1):
            move_time = value - acc_time
            moved_distance = acc_time * move_time
            if moved_distance > record:
                counter += 1

        print(counter)
        counters.append(counter)

    print(multiply(counters))


def task_6_2(lines):
    lines = map(lambda x: x.replace(" ", ""), lines)
    task_6_1(list(lines))


def get_numbers(line):
    numbers = map(int, re.findall('[0-9]+', line))
    return list(numbers)


def multiply(array):
    result = 1
    for element in array:
        result *= element

    return result
