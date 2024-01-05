def task_4_1(lines):
    points = []
    for line in lines:
        line = line.replace('\n', '')
        beginning = line.find(':')
        line = line[beginning + 1:]
        sets = line.split("|")
        winning = list(map(int, filter(lambda x: x.isdigit(), sets[0].split(" "))))
        chosen = list(map(int, filter(lambda x: x.isdigit(), sets[1].split(" "))))

        incrementer = 0
        for number in chosen:
            if number in winning:
                incrementer += 1

        if incrementer > 0:
            card_value = 1
        else:
            points.append(0)
            continue

        for i in range(1, incrementer):
            card_value *= 2

        points.append(card_value)

    # print(points)
    print(sum(points))


def task_4_2(lines):
    points = []
    for line in lines:
        line = line.replace('\n', '')
        beginning = line.find(':')
        line = line[beginning + 1:]
        sets = line.split("|")
        winning = list(map(int, filter(lambda x: x.isdigit(), sets[0].split(" "))))
        chosen = list(map(int, filter(lambda x: x.isdigit(), sets[1].split(" "))))

        incrementer = 0
        for number in chosen:
            if number in winning:
                incrementer += 1

        points.append(incrementer)

    copies = []
    for line in lines:
        copies.append(0)

    for line_number, line in enumerate(lines):
        include_card(line_number, copies, points)

    print(sum(copies))


def include_card(card_number, copies, points):
    copies[card_number] = copies[card_number] + 1
    card_points = points[card_number]
    for card in range(card_number + 1, card_number + 1 + card_points):
        include_card(card, copies, points)
