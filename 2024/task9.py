import numpy as np


def part1(lines):
    content =[];
    for letter in lines[0].strip('\n'):
        content.append(int(letter))
    array = np.array(content)
    print(array)

    result = []

    id = 0
    is_file = True
    for i in array:
        for j in range(i):
            if is_file:
                result.append(id)
            else:
                result.append('.')

        is_file = not is_file

        if is_file:
            id += 1
    
    # print(result)

    counter = 0
    pointer = len(result) - 1
    for i in range(len(result)):
        if i == pointer and result[i] == '.':
            break
        
        if i == pointer:
            counter += i*result[i]
            break

        if result[i] != '.':
            counter += i*result[i]
        else:
            for j in range(pointer, i, -1):
                pointer -= 1
                if result[j] == '.':
                    continue
                else:
                    counter += i* result[j]
                    break

        if i == pointer:
            break;

    print(counter)



def part2(lines):
    content =[];
    for letter in lines[0].strip('\n'):
        content.append(int(letter))
    array = np.array(content)

    result = []

    id = 0
    is_file = True
    for i in array:
        for j in range(i):
            if is_file:
                result.append(id)
            else:
                result.append('.')

        is_file = not is_file

        if is_file:
            id += 1

    pointer = len(result) - 1
    while pointer > 0:
        number_indexes = find_numbers(result, pointer)

        if len(number_indexes) == 0: break;
        gap_indexes = find_gap(result, len(number_indexes), min(number_indexes))

        for i in gap_indexes:
            result[i] = result[number_indexes[0]]

        if  len(gap_indexes)>0:
            for i in number_indexes:
                result[i] = '.'

        if len(number_indexes) == 0: break;
        pointer = min(number_indexes) - 1

    counter = 0

    for i in range(len(result)):
        if result[i] == '.': continue;
        counter += result[i] * i
    
    print(counter)
    


def find_gap(array, size, max_index):
    for i in range(max_index ):
        if array[i] != '.': continue

        is_found = True
        result = []
        for j in range(size):
            if array[i+j] != '.': 
                is_found = False
                break
            result.append(i+j)
        
        if is_found:
            return result
    return []

def find_numbers(array, pointer):
    number = 0
    result = []
    for i in range(pointer, 0, -1):
        if array[i] == '.': continue

        number = array[i]
        
        for j in range(i, 0, -1):
            if array[j]!=number: return result

            result.append(j)
    return result

        



