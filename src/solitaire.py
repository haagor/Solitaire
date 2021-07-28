import matplotlib.pyplot as plt


# init

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

for k, v in board.items():
	if v == 1:
		plt.scatter(k[0], k[1], color='red')
	else:
		plt.scatter(k[0], k[1], color='white')

plt.axis([-1, 7, -1, 7])
# plt.show()

