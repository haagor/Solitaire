import matplotlib.pyplot as plt
import random
import copy


def init_board():
	board = dict()
	for x in range(7):
		for y in range(7):
			board[(x, y)] = 1

	border = [
		(0, 0), (0, 1), (1,0),
		(6, 6), (6, 5), (5, 6),
		(0, 5), (0, 6), (1, 6),
		(5, 0), (6, 0), (6, 1)
		]
	for i in border:
		del board[i]

	return board

def display(p_board):
	for k, v in p_board.items():
		if v == 1:
			plt.scatter(k[0], k[1], color='red')
		else:
			plt.scatter(k[0], k[1], color='grey')

	plt.axis([-1, 7, -1, 7])
	plt.show()

def find_moves(p_board):
	moves = []
	direction =[(0, 1), (1, 0), (0, -1), (-1, 0)]
	for k, v in p_board.items():
		if v == 0:
			continue
		else:
			for i in direction:
				slot = p_board.get((int(k[0] + i[0]), int(k[1]) + i[1]))
				if slot is not None and slot == 1:
					slot = p_board.get((k[0] + i[0] * 2, k[1] + i[1] * 2))
					if slot is not None and slot == 0:
						moves.append((k, (k[0] + i[0] * 2, k[1] + i[1] * 2)))
	return moves

def exec_move(p_board, move):
	p_board[move[0]] = 0
	p_board[move[1]] = 1
	if move[0][0] > move[1][0]:
		p_board[(move[0][0] -1, move[0][1])] = 0
	elif move[0][0] < move[1][0]:
		p_board[(move[0][0] + 1, move[0][1])] = 0
	else:
		if move[0][1] > move[1][1]:
			p_board[(move[0][0], move[0][1] - 1)] = 0
		elif move[0][1] < move[1][1]:
			p_board[(move[0][0], move[0][1] + 1)] = 0
		else:
			print("ERROR")
	return p_board

def count_ball(p_board):
	count = 0
	for k, v in p_board.items():
		count += v
	return count

def find_opti_moves(p_board, p_moves):
	res_moves = []
	possibility = 0
	cp_board = copy.deepcopy(p_board)
	for move in p_moves:
		board_tmp = exec_move(cp_board, move)
		mvs = len(find_moves(board_tmp))
		if mvs > possibility:
			possibility = mvs
			res_moves = [move]
		elif possibility == mvs:
			res_moves.append(move)
		cp_board = copy.deepcopy(p_board)
	return res_moves

def find_no_suicide_moves(p_board, p_moves):
	res_moves = []
	possibility = 0
	cp_board = copy.deepcopy(p_board)
	if count_ball(cp_board) == 2:
		return p_moves
	for move in p_moves:
		board_tmp = exec_move(cp_board, move)
		mvs = len(find_moves(board_tmp))
		if mvs > 0:
			res_moves.append(move)
		cp_board = copy.deepcopy(p_board)
	return res_moves


remaining = -1
count = 0
memory_moves = []
while remaining != 1:

	# init

	memory_moves = []
	board = init_board()

	# round 0

	board[(3, 3)] = 0

	# rounds

	opti_moves = find_moves(board)
	moves = 1
	while moves and opti_moves:
		rand = random.randint(0, len(opti_moves) - 1)
		board = exec_move(board, opti_moves[rand])
		memory_moves.append(opti_moves[rand])
		moves = find_moves(board)
		opti_moves = moves
		if remaining < 16:
			opti_moves = find_no_suicide_moves(board, moves)

	remaining = count_ball(board)
	count += 1

	if remaining < 4:
		print(remaining, end = '', flush=True)
	elif count % 1000 == 0:
		print(".", end = '', flush=True)

print("VICTORY!")
print(memory_moves)



