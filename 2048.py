from random import randint

from itertools import combinations

rows_compilation = [['    ', '    ', '    ', '    '], ['    ', '    ', '    ', '    '], ['    ', '    ', '    ', '    '], ['    ', '    ', '    ', '    ']]

all_coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]

for each in [x for x in combinations(all_coordinates, 2)][randint(0, len([x for x in combinations(all_coordinates, 2)]) - 1)]:
    rows_compilation[each[0]][each[1]] = str([2, 4][randint(0, 1)]) + '   '


def continue_or_game_over():
  for rows in rows_compilation:
        for horizontal in range(0, 3):
            if rows[horizontal] != rows[horizontal + 1] and '    ' not in all_squares:
                pass
            else:
                return
    for vertical in range(0, 4):
        for rows in range(0, 3):
            if rows_compilation[rows][vertical] != rows_compilation[rows + 1][vertical] and '    ' not in all_squares:
                pass
            else:
                return
    print(rows_compilation[0][0], rows_compilation[0][1], rows_compilation[0][2], rows_compilation[0][3])
    print(rows_compilation[1][0], rows_compilation[1][1], rows_compilation[1][2], rows_compilation[1][3])
    print(rows_compilation[2][0], rows_compilation[2][1], rows_compilation[2][2], rows_compilation[2][3])
    print(rows_compilation[3][0], rows_compilation[3][1], rows_compilation[3][2], rows_compilation[3][3])
    print('game over')
    exit()


def movement():
    if move == 'w':
        for column in range(4):
            not_empty = -1
            for rows in rows_compilation:
                if rows[column] != '    ':
                    not_empty += 1
                    rows_compilation[not_empty][column] = rows[column]
                else:
                    pass
            if -1 < not_empty < 3:
                while not_empty - 3 < 0:
                    rows_compilation[not_empty - 3][column] = '    '
                    not_empty += 1
            else:
                pass
    elif move == 's':
        for column in range(4):
            not_empty = 4
            for rows in [3, 2, 1, 0]:
                if rows_compilation[rows][column] != '    ':
                    not_empty -= 1
                    rows_compilation[not_empty][column] = rows_compilation[rows][column]
                else:
                    pass
            if 0 < not_empty < 4:
                while not_empty > 0:
                    rows_compilation[not_empty - 1][column] = '    '
                    not_empty -= 1
            else:
                pass
    elif move == 'a':
        for rows in rows_compilation:
            a = 0
            if rows.count('    ') != 4:
                not_empty = 4 - rows.count('    ')
                b = 0
                while a < not_empty:
                    if rows[b] != '    ':
                        rows[a] = rows[b]
                        a += 1
                    else:
                        pass
                    b += 1
                for index, empty in enumerate(rows[not_empty:]):
                    if empty != '    ':
                        rows[not_empty + index] = '    '
    elif move == 'd':
        for rows in rows_compilation:
            a = 0
            if rows.count('    ') != 4:
                not_empty = 4 - rows.count('    ')
                b = -1
                while a < not_empty:
                    if rows[b] != '    ':
                        rows[-a - 1] = rows[b]
                        a += 1
                    else:
                        pass
                    b -= 1
                for index, empty in enumerate(rows[:(4 - not_empty)]):
                    if empty != '    ':
                        rows[index] = '    '
        else:
            pass
    else:
        pass


def merge():
    for rows in rows_compilation:
        if rows.count('    ') <= 2:
            if move == 'a':
                for if_same in range(3):
                    if rows[if_same] == rows[if_same + 1] and rows[if_same] != '    ':
                        rows[if_same] = str(2 * int(rows[if_same].strip())) + (4 - len(str(2 * int(rows[if_same].strip())))) * ' '
                        rows[if_same + 1] = '    '
                    else:
                        pass
                for alignment in [0, 1]:
                    if rows[alignment + 1] == '    ' and rows[alignment + 2] != '    ':
                        rows[alignment + 1] = rows[alignment + 2]
                        rows[alignment + 2] = '    '
                    else:
                        pass
            elif move == 'd':
                for if_same in [3, 2, 1]:
                    if rows[if_same] == rows[if_same - 1] and rows[if_same] != '    ':
                        rows[if_same] = str(2 * int(rows[if_same].strip())) + (4 - len(str(2 * int(rows[if_same].strip())))) * ' '
                        rows[if_same - 1] = '    '
                    else:
                        pass
                for alignment in [3, 2]:
                    if rows[alignment - 1] == '    ' and rows[alignment - 2] != '    ':
                        rows[alignment - 1] = rows[alignment - 2]
                        rows[alignment - 2] = '    '
                    else:
                        pass
        else:
            pass
    for column in range(4):
        if move == 'capacity':
            for if_same in range(3):
                if rows_compilation[if_same][column] == rows_compilation[if_same + 1][column] and rows_compilation[if_same][column] != '    ':
                    rows_compilation[if_same][column] = str(2 * int(rows_compilation[if_same][column].strip())) + (4 - len(str(2 * int(rows_compilation[if_same][column].strip())))) * ' '
                    rows_compilation[if_same + 1][column] = '    '
                else:
                    pass
            for alignment in [0, 1]:
                if rows_compilation[alignment + 1][column] == '    ' and rows_compilation[alignment + 2][column] != '    ':
                    rows_compilation[alignment + 1][column] = rows_compilation[alignment + 2][column]
                    rows_compilation[alignment + 2][column] = '    '
                else:
                    pass
        elif move == 's':
            for if_same in [3, 2, 1]:
                if rows_compilation[if_same][column] == rows_compilation[if_same - 1][column] and rows_compilation[if_same][column] != '    ':
                    rows_compilation[if_same][column] = str(2 * int(rows_compilation[if_same][column].strip())) + (4 - len(str(2 * int(rows_compilation[if_same][column].strip())))) * ' '
                    rows_compilation[if_same - 1][column] = '    '
                else:
                    pass
            for alignment in [3, 2]:
                if rows_compilation[alignment - 1][column] == '    ' and rows_compilation[alignment - 2][column] != '    ':
                    rows_compilation[alignment - 1][column] = rows_compilation[alignment - 2][column]
                    rows_compilation[alignment - 2][column] = '    '
                else:
                    pass


def generate_number():
    empty_compilation = list()
    row_empty = 0
    column_empty = 0
    for if_empty in all_squares:
        if if_empty == '    ':
            empty_compilation.append([row_empty, column_empty])
            column_empty += 1
            if column_empty == 4:
                column_empty = 0
                row_empty += 1
            else:
                pass
        else:
            column_empty += 1
            if column_empty == 4:
                column_empty = 0
                row_empty += 1
            else:
                pass
    generation = empty_compilation[randint(0, len(empty_compilation) - 1)]
    rows_compilation[generation[0]][generation[1]] = str([2, 4][randint(0, 1)]) + '   '


database = list()
while True:
    database.append(str(rows_compilation))
    print(rows_compilation[0][0], rows_compilation[0][1], rows_compilation[0][2], rows_compilation[0][3])
    print(rows_compilation[1][0], rows_compilation[1][1], rows_compilation[1][2], rows_compilation[1][3])
    print(rows_compilation[2][0], rows_compilation[2][1], rows_compilation[2][2], rows_compilation[2][3])
    print(rows_compilation[3][0], rows_compilation[3][1], rows_compilation[3][2], rows_compilation[3][3])
    move = input('w: up, a: left, s: down, d: right ———— ')
    movement()
    merge()
    database.append(str(rows_compilation))
    all_squares = [x for y in rows_compilation for x in y]
    if '    ' in all_squares and database[0] != database[-1]:
        generate_number()
        all_squares = [x for y in rows_compilation for x in y]
        continue_or_game_over()
    else:
        pass
    database.clear()

