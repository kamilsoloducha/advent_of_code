from functools import cmp_to_key
from math import floor


def part2(lines):
    rules = []
    rules_int = []

    pages_set = []

    counter = 0

    for i in range(len(lines)):
        line: str = lines[i]

        if line.find('|') > 0:
            rules_int.append(list(map(int, line.split('|'))))
            rules.append(line.strip('\n'))

        if line.find(',') > 0:
            pages_set.append(list(map(int, line.split(','))))
    
    for pages in pages_set:
        is_correct = True
        for i in range(len(pages)):

            for j in range(len(pages)):

                if i == j:
                    continue

                if j < i:
                    rule_to_check = str(pages[j]) + '|' + str(pages[i])

                    is_correct = is_correct and rule_to_check in rules

                if j > i:
                    rule_to_check = str(pages[i]) + '|' + str(pages[j])

                    is_correct = is_correct and rule_to_check in rules

                if not is_correct:
                    break;
        
        if not is_correct:
            filtered_rules = []

            for rule in rules_int:
                if rule[0] in pages and rule[1] in pages:
                    filtered_rules.append(rule)

            sorted_pages = sorted(pages, key=cmp_to_key(lambda item1, item2: compare(item1, item2, filtered_rules)))
            print(sorted_pages)
            print(sorted_pages[floor(len(sorted_pages) / 2)])
            
            counter += sorted_pages[floor(len(sorted_pages) / 2)]

    print(counter)

def compare(x, y, rules):
    for rule in rules:
        if not x in rule or not y in rule:
            continue

        if rule[0] == x and rule[1] == y:
            return -1
        else:
            return 1









def part1(lines):
    rules = []

    pages_set = []

    counter = 0

    for i in range(len(lines)):
        line: str = lines[i]

        if line.find('|') > 0:
            # rules.append(list(map(int, line.split('|'))))
            rules.append(line.strip('\n'))

        if line.find(',') > 0:
            pages_set.append(list(map(int, line.split(','))))
    
    for pages in pages_set:
        is_correct = True
        for i in range(len(pages)):

            for j in range(len(pages)):

                if i == j:
                    continue

                if j < i:
                    rule_to_check = str(pages[j]) + '|' + str(pages[i])

                    is_correct = is_correct and rule_to_check in rules

                if j > i:
                    rule_to_check = str(pages[i]) + '|' + str(pages[j])

                    is_correct = is_correct and rule_to_check in rules

                if not is_correct:
                    break;
        
        if is_correct:
            counter += pages[int(len(pages) / 2)]
    
    print(counter)

