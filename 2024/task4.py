import numpy as np

def part1(lines):
    content = list(map(lambda x: [y for y in x.strip('\n')], lines))
    array = np.array(content)

    counter = 0

    for i in range(len(array)):
        for j in range(len(array[i])):

            curr_char = array[i][j];
            
            if curr_char == 'X':
                if checkHorizontal(array, i, j, 'XMAS'):
                    counter += 1
                if checkVertical(array, i, j, 'XMAS'):
                    counter += 1
                if checkDiagonalUp(array, i, j, 'XMAS'):
                    counter += 1
                if checkDiagonalDown(array, i, j, 'XMAS'):
                    counter += 1
                continue

            if curr_char == 'S':
                if checkHorizontal(array, i, j, 'SAMX'):
                    counter += 1
                if checkVertical(array, i, j, 'SAMX'):
                    counter += 1
                if checkDiagonalUp(array, i, j, 'SAMX'):
                    counter += 1
                if checkDiagonalDown(array, i, j, 'SAMX'):
                    counter += 1
                continue
    
    print(counter)


def part2(lines):
    content = list(map(lambda x: [y for y in x.strip('\n')], lines))
    array = np.array(content)
    print(array)

    counter = 0

    for i in range(1, len(array) - 1):
        for j in range(1, len(array[i]) - 1):

            curr_char = array[i][j];

            if curr_char != 'A':
                continue

            if (checkDiagonalDown2(array, i - 1, j-1, 'MAS') or checkDiagonalDown2(array, i -1, j-1, 'SAM')) and (
                checkDiagonalUp2(array, i + 1, j-1, 'MAS') or checkDiagonalUp2(array, i +1, j-1, 'SAM')):
                counter +=1
    print(counter)


                
def checkHorizontal(array, x, y, searching):
    if y > len(array[1]) - 4: 
        return False
    word = array[x][y] + array[x][y+1]+array[x][y+2]+array[x][y+3]
    return word == searching

def checkVertical(array, x, y, searching):
    if x > len(array) - 4: 
        return False
    word = array[x][y] + array[x+1][y]+array[x+2][y]+array[x+3][y]
    return word == searching

def checkDiagonalUp(array, x, y, searching):
    if x < 3 or y > len(array[1]) - 4: 
        return False
    word = array[x][y] + array[x-1][y+1]+array[x-2][y+2]+array[x-3][y+3]
    return word == searching

def checkDiagonalDown(array, x, y, searching):
    if x > len(array) - 4 or y > len(array[1]) - 4: 
        return False
    word = array[x][y] + array[x+1][y+1]+array[x+2][y+2]+array[x+3][y+3]
    return word == searching

def checkDiagonalUp2(array, x, y, searching):
    word_len = len(searching)
    if x - word_len + 1 < 0 or y > len(array[1]) - word_len: 
        return False
    word = ''
    for i in range(word_len):
        word += array[x-i][y+i]
    return word == searching

def checkDiagonalDown2(array, x, y, searching):
    word_len = len(searching)
    if x > len(array) - word_len or y > len(array[1]) - word_len: 
        return False
    word = ''
    for i in range(word_len):
        word += array[x+i][y+i]
    return word == searching

