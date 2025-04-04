def part1(lines):

    blinks = 75
    numbers = list(map(int, lines[0].strip('\n').split(' ')))
    
    for i in range(blinks):
        print(i)
        new_numbers = []
        for number in numbers:

            if number ==0:
                new_numbers.append(1)
                continue

            length = len(str(number))
            if length % 2 == 0:
                new_numbers.append(int(str(number)[0:int(length /2)]))
                new_numbers.append(int(str(number)[int(length /2) : length]))
                continue

            new_numbers.append(number * 2024)

        numbers = new_numbers

    print(len(numbers))
