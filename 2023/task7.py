from functools import cmp_to_key


def task_7_1(lines):
    hands = []

    for line in lines:
        hands.append(Hand(line))

    hands = sorted(hands, key=cmp_to_key(compare))

    sum = 0

    for i, hand in enumerate(hands):
        increase = (i+1)*hand.bid
        sum += increase

    print(sum)


def task_7_2(lines):
    hands = []

    for line in lines:
        hands.append(HandNew(line))

    hands = sorted(hands, key=cmp_to_key(compare_2))

    sum = 0

    for i, hand in enumerate(hands):
        increase = (i + 1) * hand.bid
        sum += increase

    print(sum)


def get_bid(line: str):
    return int(line[6:])


def get_cards(line: str):
    return line[0:5]


def map_to_int(char: str):
    match char:
        case "A":
            return 13
        case "K":
            return 12
        case "Q":
            return 11
        case "J":
            return 10
        case "T":
            return 9
        case "9":
            return 8
        case "8":
            return 7
        case "7":
            return 6
        case "6":
            return 5
        case "5":
            return 4
        case "4":
            return 3
        case "3":
            return 2
        case "2":
            return 1
    print('error')


def map_to_int_2(char: str):
    match char:
        case "A":
            return 13
        case "K":
            return 12
        case "Q":
            return 11

        case "T":
            return 9
        case "9":
            return 8
        case "8":
            return 7
        case "7":
            return 6
        case "6":
            return 5
        case "5":
            return 4
        case "4":
            return 3
        case "3":
            return 2
        case "2":
            return 1
        case "J":
            return 0
    print('error')


def compare(self, other):
    if self.type != other.type:
        return self.type - other.type

    index = 0
    for i in range(0, 6):
        if self.line[i] != other.line[i]:
            index = i
            break

    return map_to_int(self.line[index]) - map_to_int(other.line[index])


def compare_2(self, other):
    if self.type != other.type:
        return self.type - other.type

    index = 0
    for i in range(0, 6):
        if self.line[i] != other.line[i]:
            index = i
            break

    value1 = map_to_int_2(self.line[index])
    value2 = map_to_int_2(other.line[index])

    return value1 - value2


def get_type(cards: str):
    card_map = {}
    for char in cards:
        if card_map.get(char) is None:
            card_map[char] = 1
        else:
            card_map[char] += 1

    card_map = list(sorted(card_map.items(), key=lambda x: x[1], reverse=True))
    if card_map[0][1] == 5:
        return 7

    if card_map[0][1] == 4:
        return 6

    if card_map[0][1] == 3 and card_map[1][1] == 2:
        return 5

    if card_map[0][1] == 3:
        return 4

    if card_map[0][1] == 2 and card_map[1][1] == 2:
        return 3

    if card_map[0][1] == 2:
        return 2

    return 1


def get_type_new(cards: str):
    card_map = {}
    for char in cards:
        if card_map.get(char) is None:
            card_map[char] = 1
        else:
            card_map[char] += 1

    jokers = 0

    if card_map.get('J') is not None:
        jokers = card_map['J']

    card_map = list(sorted(card_map.items(), key=lambda x: x[1], reverse=True))
    if card_map[0][1] == 5:
        return 7

    if card_map[0][1] == 4:
        if jokers == 4:
            return 7
        if jokers == 0:
            return 6
        else:
            return 7

    if card_map[0][1] == 3 and card_map[1][1] == 2:
        if jokers == 0:
            return 5
        else:
            return 7

    if card_map[0][1] == 3:
        if jokers == 3:
            return 6
        if jokers == 0:
            return 4
        else:
            return 6

    if card_map[0][1] == 2 and card_map[1][1] == 2:
        if jokers == 0:
            return 3
        if jokers == 1:
            return 5
        if jokers == 2:
            return 6

    if card_map[0][1] == 2:
        if jokers == 2:
            return 4
        if jokers == 0:
            return 2
        if jokers == 1:
            return 4

    if jokers == 1:
        return 2

    return 1


class Hand:
    line = ""
    bid = 0
    type = 0

    def __init__(self, line):
        self.line = line.replace('\n', '')
        self.bid = get_bid(line)
        self.type = get_type(get_cards(line))

    def __str__(self):
        return f'[{self.line}: {self.bid}] - {self.type}'

    def __repr__(self):
        return str(self)


class HandNew:
    line = ""
    bid = 0
    type = 0

    def __init__(self, line):
        self.line = line.replace('\n', '')
        self.bid = get_bid(line)
        self.type = get_type_new(get_cards(line))

    def __str__(self):
        return f'[{self.line}: {self.bid}] - {self.type}'

    def __repr__(self):
        return str(self)
