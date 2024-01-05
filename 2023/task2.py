import re
import sys

maxRed = 12
maxGreen = 13
maxBlue = 14


def task_2_1(content):
    sum = 0
    line_number = 1

    for line in content:
        is_possible = True
        beginning = line.find(":")
        colors = re.split("; |, ", line[beginning + 1:])

        for color in colors:
            number_str = re.findall('[0-9]+', color)[0]
            number = int(number_str)

            if is_possible and color.find("red") >= 0 and number > maxRed:
                is_possible = False

            if is_possible and color.find("green") >= 0 and number > maxGreen:
                is_possible = False

            if is_possible and color.find("blue") >= 0 and number > maxBlue:
                is_possible = False

        if is_possible:
            sum += line_number

        line_number += 1

    print(sum)

    return sum


def task_2_2(content):
    sum = 0

    for line in content:
        beginning = line.find(":")
        colors = re.split("; |, ", line[beginning + 1:])

        max_red = 0
        max_green = 0
        max_blue = 0

        for color in colors:
            number_str = re.findall('[0-9]+', color)[0]
            found_number = int(number_str)

            if color.find("red") >= 0 and found_number >= max_red:
                max_red = found_number
            if color.find("green") >= 0 and found_number >= max_green:
                max_green = found_number
            if color.find("blue") >= 0 and found_number >= max_blue:
                max_blue = found_number

        power = max_red * max_blue * max_green
        sum += power

    print(sum)

    return sum
