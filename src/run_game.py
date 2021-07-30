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



board = init_board()
board[(3, 4)] = 0

record = [((1, 4), (3, 4)), ((2, 2), (2, 4)), ((4, 3), (2, 3)), ((4, 5), (4, 3)), ((6, 4), (4, 4)), ((6, 2), (6, 4)), ((2, 0), (2, 2)), ((2, 3), (2, 1)), ((4, 0), (2, 0)), ((3, 2), (3, 0)), ((5, 1), (3, 1)), ((0, 3), (2, 3)), ((1, 1), (1, 3)), ((3, 4), (1, 4)), ((2, 6), (2, 4)), ((3, 6), (3, 4)), ((3, 4), (5, 4)), ((6, 4), (4, 4)), ((4, 3), (4, 5)), ((4, 6), (4, 4)), ((5, 2), (5, 4)), ((3, 0), (3, 2)), ((2, 0), (2, 2)), ((3, 2), (1, 2)), ((0, 2), (2, 2)), ((1, 4), (3, 4)), ((5, 5), (5, 3)), ((3, 4), (5, 4)), ((5, 4), (5, 2)), ((5, 2), (3, 2)), ((3, 2), (1, 2)), ((1, 2), (1, 4)), ((0, 4), (2, 4)), ((2, 3), (2, 5)), ((1, 5), (3, 5))]

for move in record:
	exec_move(board, move)
	display(board)



