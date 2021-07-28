import matplotlib.pyplot as plt


def display(p_board):
	for k, v in p_board.items():
		if v == 1:
			plt.scatter(k[0], k[1], color='red')
		else:
			plt.scatter(k[0], k[1], color='white')

	plt.axis([-1, 7, -1, 7])
	plt.show()

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


# init

board = init_board()

# round 0

board[(3, 3)] = 0

# rounds

moves = []
direction =[(0, 1), (1, 0), (0, -1), (-1, 0)]
for k, v in board.items():
	if v == 0:
		continue
	else:
		for i in direction:
			slot = board.get((int(k[0] + i[0]), int(k[1]) + i[1]))
			if slot is not None and slot == 1:
				slot = board.get((k[0] + i[0] * 2, k[1] + i[1] * 2))
				if slot is not None and slot == 0:
					moves.append((k, (k[0] + i[0] * 2, k[1] + i[1] * 2)))

print(moves)


