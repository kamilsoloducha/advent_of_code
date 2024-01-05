import sys


def task_1_1(lines):
    sum = 0
    for line in lines:
        numbers = []
        for char in line:
            if char.isnumeric():
                numbers.append(char)

        sum += int(numbers[0] + numbers[-1])

    print(sum)


def task_1_2(lines):
    sum = 0
    elements = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for line in lines:
        first_element = convert(find_first(line, elements))
        last_element = convert(find_last(line, elements))

        print(line, first_element, last_element)

        sum += int(first_element + last_element)

    print(sum)


def find_first(line, elements):
    min_index = sys.maxsize
    searching_element = ""
    for element in elements:
        first_occ = line.find(element)
        if 0 <= first_occ < min_index:
            min_index = first_occ
            searching_element = element

    return searching_element


def find_last(line, elements):
    max_index = -1
    searching_element = ""
    for element in elements:
        last_occ = line.rfind(element)
        if last_occ >= 0 and last_occ > max_index:
            max_index = last_occ
            searching_element = element

    return searching_element


def convert(value):
    match value:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"
    return value