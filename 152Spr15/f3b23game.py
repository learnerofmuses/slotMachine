import random

ROW = 3
COL = 5

def build_board_random(row, col):
	board = [[0 for i in range (col+2)]for j in range (row+2)]
	for i in range(1, row):
		for j in range(1, col):
			board[i][j]=random.randint(0,1)
	return board

def main():
	print(build_board_random(ROW, COL))	
	

main()
