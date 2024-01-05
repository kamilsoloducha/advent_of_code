def task1(lines):
    numbers_array = list(map(get_numbers, lines))
    print(numbers_array)

    sum = 0
    for arr in numbers_array:
        sum += find_next(arr)

    print(sum)


def task2(lines):
    numbers_array = list(map(get_numbers, lines))

    sum = 0
    for arr in numbers_array:
        priv = find_priv(arr)
        sum += priv

    print(sum)

def get_numbers(line:str):
    return list(map(int, line.replace("\n", "").split(" ")))


def find_priv(arr):
    diff_array = find_diff(arr)
    const = 0
    if not is_const(diff_array):
        const = find_priv(diff_array)
    else:
        const = diff_array[0]

    fist_element = arr[0]
    return fist_element - const

def find_next(arr: []):
    diff_array = find_diff(arr)
    const = 0
    if not is_const(diff_array):
        const = find_next(diff_array)
    else:
        const = diff_array[0]

    last_element = arr[-1]
    return last_element + const


def find_diff(arr:[]):
    result = []
    for i in range(0,len(arr)-1):
        result.append(arr[i+1] - arr[i])

    return result


def is_const(arr: []):
    element = arr[0]
    for item in arr:
        if item != element:
            return False

    return True