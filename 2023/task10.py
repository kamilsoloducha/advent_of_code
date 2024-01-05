import util


def task1(content):
    max_x = len(content[0]) - 1
    max_y = len(content)

    start_x = 0
    start_y = 0

    for i in range(len(content)):
        for j in range(len(content[i])):
            if content[i][j] == 'S':
                start_x = j
                start_y = i

    is_closed = False
    counter = 0

    start = util.Point(start_x, start_y)
    previous = util.Point(start_x, start_y)
    current = util.Point(start_x, start_y)
    next_pos: util.Point

    is_found = False

    if content[start.y][start.x + 1] in ['-', 'J', '7']:
        current = util.Point(start_x + 1, start_y)
        is_found = True

    if content[start.y][start.x - 1] in ['-', 'F', 'L'] and not is_found:
        current = util.Point(start_x - 1, start_y)
        is_found = True

    if content[start.y + 1][start.x] in ['|', 'J', 'L'] and not is_found:
        current = util.Point(start_x, start_y + 1)
        is_found = True

    if content[start.y - 1][start.x] in ['|', 'F', '7'] and not is_found:
        current = util.Point(start_x, start_y - 1)

    next_pos = current

    while not is_closed:
        current = next_pos
        curr_direction = content[current.y][current.x]
        print(curr_direction)
        next1: util.Point = None
        next2: util.Point = None

        match curr_direction:
            case '|':
                next1 = util.Point(current.x, current.y - 1)
                next2 = util.Point(current.x, current.y + 1)
            case '-':
                next1 = util.Point(current.x - 1, current.y)
                next2 = util.Point(current.x + 1, current.y)
            case 'F':
                next1 = util.Point(current.x, current.y + 1)
                next2 = util.Point(current.x + 1, current.y)
            case 'J':
                next1 = util.Point(current.x - 1, current.y)
                next2 = util.Point(current.x, current.y - 1)
            case '7':
                next1 = util.Point(current.x, current.y + 1)
                next2 = util.Point(current.x - 1, current.y)
            case 'L':
                next1 = util.Point(current.x, current.y - 1)
                next2 = util.Point(current.x + 1, current.y)

        if previous == next1:
            next_pos = next2
        else:
            next_pos = next1
        previous = current
        counter += 1

        if next_pos == start:
            counter += 1
            is_closed = True

    print(counter / 2)
    return


def task2(content):
    content_copy = util.to_2_dim_array(content)

    start_x = 0
    start_y = 0

    for i in range(len(content)):
        for j in range(len(content[i])):
            if content[i][j] == 'S':
                start_x = j
                start_y = i

    is_closed = False
    counter = 0

    start = util.Point(start_x, start_y)
    previous = util.Point(start_x, start_y)
    current = util.Point(start_x, start_y)
    next_pos: util.Point

    content_copy[start.y][start.x] = 'P'

    is_found = False

    if content[start.y][start.x + 1] in ['-', 'J', '7']:
        current = util.Point(start_x + 1, start_y)
        is_found = True

    if content[start.y][start.x - 1] in ['-', 'F', 'L'] and not is_found:
        current = util.Point(start_x - 1, start_y)
        is_found = True

    if content[start.y + 1][start.x] in ['|', 'J', 'L'] and not is_found:
        current = util.Point(start_x, start_y + 1)
        is_found = True

    if content[start.y - 1][start.x] in ['|', 'F', '7'] and not is_found:
        current = util.Point(start_x, start_y - 1)

    next_pos = current

    while not is_closed:

        current = next_pos
        content_copy[current.y][current.x] = 'P'

        curr_direction = content[current.y][current.x]
        next1: util.Point = None
        next2: util.Point = None

        match curr_direction:
            case '|':
                next1 = util.Point(current.x, current.y - 1)
                next2 = util.Point(current.x, current.y + 1)
            case '-':
                next1 = util.Point(current.x - 1, current.y)
                next2 = util.Point(current.x + 1, current.y)
            case 'F':
                next1 = util.Point(current.x, current.y + 1)
                next2 = util.Point(current.x + 1, current.y)
            case 'J':
                next1 = util.Point(current.x - 1, current.y)
                next2 = util.Point(current.x, current.y - 1)
            case '7':
                next1 = util.Point(current.x, current.y + 1)
                next2 = util.Point(current.x - 1, current.y)
            case 'L':
                next1 = util.Point(current.x, current.y - 1)
                next2 = util.Point(current.x + 1, current.y)

        if previous == next1:
            next_pos = next2
        else:
            next_pos = next1
        previous = current

        if next_pos == start:
            is_closed = True

    # no_change = False
    #
    # while not no_change:
    #     no_change = True
    #     for i in range(len(content_copy)):
    #         for j in range(len(content_copy[i])):
    #
    #             if content_copy[i][j] in ['P', 'O']:
    #                 continue
    #
    #             if i == 0 or j == 0 or i == len(content_copy) - 1 or j == len(content_copy[i]) - 1:
    #                 content_copy[i][j] = 'O'
    #                 no_change = False
    #                 continue
    #
    #             if (content_copy[i - 1][j - 1] == 'O' or
    #                     content_copy[i][j - 1] == 'O' or
    #                     content_copy[i + 1][j - 1] == 'O' or
    #                     content_copy[i - 1][j + 1] == 'O' or
    #                     content_copy[i][j + 1] == 'O' or
    #                     content_copy[i + 1][j + 1] == 'O' or
    #                     content_copy[i - 1][j] == 'O' or
    #                     content_copy[i + 1][j] == 'O'):
    #                 content_copy[i][j] = 'O'
    #                 no_change = False
    #                 continue

    # no_change = False
    #
    # while not no_change:
    #     no_change = True
    #     for i in range(len(content_copy)):
    #         for j in range(len(content_copy[i])):
    #
    #             if content_copy[i][j] in ['P', 'O']:
    #                 continue
    #
    #             if (content_copy[i - 1][j - 1] == 'O' or
    #                     content_copy[i][j - 1] == 'O' or
    #                     content_copy[i + 1][j - 1] == 'O' or
    #                     content_copy[i - 1][j + 1] == 'O' or
    #                     content_copy[i][j + 1] == 'O' or
    #                     content_copy[i + 1][j + 1] == 'O' or
    #                     content_copy[i - 1][j] == 'O' or
    #                     content_copy[i + 1][j] == 'O'):
    #                 content_copy[i][j] = 'O'
    #                 no_change = False
    #                 continue
    #
    # # util.print_table(content_copy)
    #
    # print()
    # print()
    # print()


    check_horizontal(content, content_copy)

    # util.print_table(content_copy)

    counter = 0
    for i in range(len(content_copy)):
        for j in range(len(content_copy[i])):
            if content_copy[i][j] == 'I':
                counter += 1

    print(counter)
    return


def check_horizontal(content, content_copy):
    for i in range(len(content_copy)):
        counter = 0
        edge_start = ''
        for j in range(len(content_copy[i])):
            char = content_copy[i][j]
            if char in ['0']:
                continue

            if char == 'P':

                original_char = content[i][j]

                if original_char == '-':
                    continue

                if original_char == '|':
                    counter += 1
                    continue

                if original_char in ['L', 'F']:
                    edge_start = original_char
                    continue

                if ((edge_start == 'L' and original_char == '7') or
                        (edge_start == 'F' and original_char == 'J')):
                    counter += 1
                    edge_start = ''
                    continue
                else:
                    edge_start = ''
                    continue

            if counter % 2 == 0:
                content_copy[i][j] = 'O'
            else:
                content_copy[i][j] = 'I'


