from random import randint
from itertools import combinations
grid = [['    ' for y in range(4)] for x in range(0, 4)]
all_pos = [[x, y] for x in range(0, 4) for y in range(0, 4)]
for each in [x for x in combinations(all_pos, 2)][randint(0, len([x for x in combinations(all_pos, 2)]) - 1)]:
	grid[each[0]][each[1]] = str([2, 4][randint(0, 1)]) + '   '


def continue_or_game_over():
	if '    ' in all_cells:
		return
	else:
		for rows in grid:
			for horizontal in range(0, 3):
				if rows[horizontal] == rows[horizontal + 1]:
					return
		for vertical in range(0, 4):
			for rows in range(0, 3):
				if grid[rows][vertical] == grid[rows + 1][vertical]:
					return
		print('\n')
		print(grid[0][0], '|', grid[0][1], '|', grid[0][2], '|', grid[0][3])
		print('---------------------------')
		print(grid[1][0], '|', grid[1][1], '|', grid[1][2], '|', grid[1][3])
		print('---------------------------')
		print(grid[2][0], '|', grid[2][1], '|', grid[2][2], '|', grid[2][3])
		print('---------------------------')
		print(grid[3][0], '|', grid[3][1], '|', grid[3][2], '|', grid[3][3])
		print('game over')
		exit()


def movement():
	if move == 'w':
		for column in range(4):
			not_empty = -1
			for rows in grid:
				if rows[column] != '    ':
					not_empty += 1
					grid[not_empty][column] = rows[column]
			if -1 < not_empty < 3:
				while not_empty - 3 < 0:
					grid[not_empty - 3][column] = '    '
					not_empty += 1
	elif move == 's':
		for column in range(4):
			not_empty = 4
			for rows in [3, 2, 1, 0]:
				if grid[rows][column] != '    ':
					not_empty -= 1
					grid[not_empty][column] = grid[rows][column]
			if 0 < not_empty < 4:
				while not_empty > 0:
					grid[not_empty - 1][column] = '    '
					not_empty -= 1
	elif move == 'a':
		for rows in grid:
			a = 0
			if rows.count('    ') != 4:
				not_empty = 4 - rows.count('    ')
				b = 0
				while a < not_empty:
					if rows[b] != '    ':
						rows[a] = rows[b]
						a += 1
					b += 1
				for index, empty in enumerate(rows[not_empty:]):
					if empty != '    ':
						rows[not_empty + index] = '    '
	elif move == 'd':
		for rows in grid:
			a = 0
			if rows.count('    ') != 4:
				not_empty = 4 - rows.count('    ')
				b = -1
				while a < not_empty:
					if rows[b] != '    ':
						rows[-a - 1] = rows[b]
						a += 1
					b -= 1
				for index, empty in enumerate(rows[:(4 - not_empty)]):
					if empty != '    ':
						rows[index] = '    '
	elif move == 'q':
		print("Game over")
		exit()


def merge():
	for rows in grid:
		if rows.count('    ') <= 2:
			if move == 'a':
				for if_same in range(3):
					if rows[if_same] == rows[if_same + 1] and rows[if_same] != '    ':
						rows[if_same] = str(2 * int(rows[if_same].strip())) + (4 - len(str(2 * int(rows[if_same].strip())))) * ' '
						rows[if_same + 1] = '    '
				for alignment in [0, 1]:
					if rows[alignment + 1] == '    ' and rows[alignment + 2] != '    ':
						rows[alignment + 1] = rows[alignment + 2]
						rows[alignment + 2] = '    '
			elif move == 'd':
				for if_same in [3, 2, 1]:
					if rows[if_same] == rows[if_same - 1] and rows[if_same] != '    ':
						rows[if_same] = str(2 * int(rows[if_same].strip())) + (4 - len(str(2 * int(rows[if_same].strip())))) * ' '
						rows[if_same - 1] = '    '
				for alignment in [3, 2]:
					if rows[alignment - 1] == '    ' and rows[alignment - 2] != '    ':
						rows[alignment - 1] = rows[alignment - 2]
						rows[alignment - 2] = '    '
	for column in range(4):
		if move == 'w':
			for if_same in range(3):
				if grid[if_same][column] == grid[if_same + 1][column] and grid[if_same][column] != '    ':
					grid[if_same][column] = str(2 * int(grid[if_same][column].strip())) + (4 - len(str(2 * int(grid[if_same][column].strip())))) * ' '
					grid[if_same + 1][column] = '    '
			for alignment in [0, 1]:
				if grid[alignment + 1][column] == '    ' and grid[alignment + 2][column] != '    ':
					grid[alignment + 1][column] = grid[alignment + 2][column]
					grid[alignment + 2][column] = '    '
		elif move == 's':
			for if_same in [3, 2, 1]:
				if grid[if_same][column] == grid[if_same - 1][column] and grid[if_same][column] != '    ':
					grid[if_same][column] = str(2 * int(grid[if_same][column].strip())) + (4 - len(str(2 * int(grid[if_same][column].strip())))) * ' '
					grid[if_same - 1][column] = '    '
			for alignment in [3, 2]:
				if grid[alignment - 1][column] == '    ' and grid[alignment - 2][column] != '    ':
					grid[alignment - 1][column] = grid[alignment - 2][column]
					grid[alignment - 2][column] = '    '


def generate_number():
	empty_tiles = list()
	row_empty = 0
	column_empty = 0
	for if_empty in all_cells:
		if if_empty == '    ':
			empty_tiles.append([row_empty, column_empty])
		column_empty += 1
		if column_empty == 4:
			column_empty = 0
			row_empty += 1
	new_pos = empty_tiles[randint(0, len(empty_tiles) - 1)]
	grid[new_pos[0]][new_pos[1]] = str([2, 4][randint(0, 1)]) + '   '


prev_cur = list()
while True:
	prev_cur.append(str(grid))
	print('\n')
	print(grid[0][0], '|', grid[0][1], '|', grid[0][2], '|', grid[0][3])
	print('--------------------------')
	print(grid[1][0], '|', grid[1][1], '|', grid[1][2], '|', grid[1][3])
	print('--------------------------')
	print(grid[2][0], '|', grid[2][1], '|', grid[2][2], '|', grid[2][3])
	print('--------------------------')
	print(grid[3][0], '|', grid[3][1], '|', grid[3][2], '|', grid[3][3])
	move = input('w: up, a: left, s: down, d: right, q: quit ———— ')
	movement()
	merge()
	prev_cur.append(str(grid))
	all_cells = [x for y in grid for x in y]
	if '    ' in all_cells and prev_cur[0] != prev_cur[-1]:
		generate_number()
		all_cells = [x for y in grid for x in y]
		continue_or_game_over()
	prev_cur.clear()
