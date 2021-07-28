import matplotlib.pyplot as plt
import random


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


remaining = -1
while remaining != 1:

	# init

	board = init_board()

	# round 0

	board[(3, 3)] = 0

	# rounds

	moves = find_moves(board)
	while moves:
		rand = random.randint(0, len(moves) - 1)
		board = exec_move(board, moves[rand])
		moves = find_moves(board)

	remaining = count_ball(board)
	if remaining < 4:
		print(remaining, end = '')
	else:
		print(".", end = '')

print("VICTORY!")



