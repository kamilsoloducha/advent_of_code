
def task2(content):
    content = content[0].replace('\n', '')
    elements = content.split(',')
    boxs = {}
    sum = 0
    for element in elements:
        lens_number = -1
        if element[-1] == '-':
            lens_label = element.strip('-')
        else:
            move = element.split('=')
            lens_label = move[0]
            lens_number = move[1]

        hash = find_hash(lens_label)
        print(element, lens_label, lens_number, hash)

        if lens_number == -1:
            if hash in boxs:
                items = boxs[hash]
                considered = find_in(items, lens_label)
                if considered is not None:
                    items.remove(considered)
        else:
            if hash in boxs:
                items = boxs[hash]
                considered = find_in(items, lens_label)
                if considered is not None:
                    considered.number = int(lens_number)
                    continue
                items.append(Lens(lens_label, lens_number))
            else:
                boxs[hash] = [Lens(lens_label, lens_number)]
    sum = 0
    for i in range(0, 256):
        if i not in boxs:
            continue

        items = boxs[i]

        if len(items) == 0:
            continue

        for j in range(len(items)):
            sum += ((i+1) * (j+1) * items[j].number)

    print(sum)


def task1(content):
    content = content[0].replace('\n', '')
    elements = content.split(',')

    sum = 0
    for element in elements:
        find_hash(element)
    print(sum)


def find_hash(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value


def find_in(arr, label):
    for x in arr:
        if x.label == label:
            return x
    return None


class Lens:
    label = ''
    number = -1

    def __init__(self, label, number):
        self.label = label
        self.number = int(number)

    def __str__(self):
        return f'[{self.label}, {self.number}]'

    def __repr__(self):
        return str(self)
