import math

def task1(lines):
    col1 = []
    col2 = []

    for line in lines:
        elements = line.replace('\n', '').split("   ")
        col1.append(int(elements[0]))
        col2.append(int(elements[1]))
    
    col1 = col1.sort()
    col2 = col2.sort()

    result = 0;

    for x in range(len(col1)):
        result += abs(col1[x] - col2[x])

    print(result) 

def task2(lines):
    print('test')
