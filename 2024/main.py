import sys;

import task1;
import task4;
import task5;
import task6;
import task7;
import task8;
import task9;
import task10;
import task11;
import task12;

# args = sys.argv[1].split(' ')
# puzzle_number = args[0];
# task_number = args[1];

file_name = './puzzles/puzzle12';

file = open(file_name, 'r')
content = file.readlines()


task12.part2(content)

# match puzzle_number:
#     case '1':
#         match task_number:
#             case '1':
#                 task1.task1(content)
#             case '2':
#                 task1.task2(content)