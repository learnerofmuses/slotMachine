#def make_new_board(oldBoard, row, col) which has three parameters, 2D 
#list with configuration at time T-1. The function creates and returns a 
#new board - configuration at time T, using the rules of the game. This 
#function will use function neigh from lab 8.

#MAIN function for Level 1: Ask user to enter 1 to randomly generate 
#initial configuration, and 0 for user input. Create a new configuration 
#for Time 1 using function make_new_board. Find if it was change in 
#configuration and print the number of live organisms at Time 0 and Time 
#1.

#MAIN function for Level 2: Ask user to enter 1 to randomly generate 
#initial configuration, and 0 for user input. Create a new configuration 
#for Time 1, then at Time 2 and Time 3. Find if it was change in 
#configuration at each time and print the number of live organisms at 
#each time.

import random 

ROW = 2
COL = 4

def build_board_random(row, col):
	board=[[0 for i in range (col+2)]for j in range (row+2)]
	for i in range(1, row+1):
		for j in range(1, col+1):
			board[i][j]=random.randint(0,1)
	return board

def build_board_user(row, col):
	user_board=[[0 for i in range (col+2)]for j in range (row+2)]
	for i in range(1, row+1):
		for j in range(1, col+1):
			user_board[i][j]=int(input("please enter 0 or 1: "))
	print("user board: ")
	return user_board

def printBoard(board, row, col):
	for i in range(1, row+1):
		for j in range(1, col+1):
			print(board[i][j], end= " ")
	print()

def printFullBoard(board, row, col):
	for i in range(row+2):
		print(board[i])

def copyBoard(board, row, col):
	new_board=[[0 for i in range (col+2)] for j in range (row+2)]
	for i in range(row+2):
		for j in range(col+2):
			new_board[i][j]=board[i][j]
	print("changed board: ")
	return new_board

def change(oldBoard, newBoard, row, col):
	count = 0 
	for i in range(1, row+1):
		for j in range(1, col+1):
			if(oldBoard[i][j]==newBoard[i][j]):
				count+=1
	if(count == (row*col)):
		res = 1
		print("didn't change")
	else:
		res = 0 
		print("did change")
	return res 
def count(board, row, col):
	lives = 0 
	for i in range(1, row+1):
		for j in range(1, col+1):
			if(board[i][j]==1):
				lives+=1
		return lives

def neigh(board, row, col, i, j):
	count = board[i-1][j]+board[i+1][j]+board[i][j-1]+board[i][j+1]
	count = count+board[i-1][j-1]+board[i-1][j+1]+board[i+1][j-1]+board[i+1][j+1]
	return count

def all_neigh(board, row, col):
	neigh_board=[[0 for i in range (col+2)] for j in range (row+2)]
	for i in range(1, row+1):
		for j in range(1, col+1):
			neigh_board=neigh[i][j](board, row, col, i, j)
	return neigh_board

def make_new_board(oldBoard, row, col):
	board =[[0 for i in range (col+2)] for j in range (row+2)] 
	sums = all_neigh(oldBoard, row, col)
	for i in range(row):
		for j in range(col):
			if oldBoard[i][j] == 0 and sum[i][j]==3:
				board[i][j]= 1
			elif oldBoard[i][j] == 1 and (sums[i][j]==2 or sums[i][j]==3):
				board[i][j]= 1
			elif oldBoard[i][j] == 1 and sums[i][j]<2:
				board[i][j]= 0
			elif oldBoard[i][j] == 1 and sums[i][j]>3:
				board[i][j]= 0
			else:
				board[i][j]= 0
  
	#change(oldBoard, board, row, col)
	return board 
  
def main():
	#this prints the random board
	print("random board: ")
	board = build_board_random(ROW, COL)
	printFullBoard(board,ROW,COL)

	#this prints the user made board
	#user_board = [[0 for i in range(COL)]for j in range(ROW)]
	user_board = build_board_user(ROW, COL)
	printFullBoard(board, ROW, COL)

	#this prints board and full board
	printBoard(board, ROW, COL)
	printFullBoard(board, ROW, COL)

	print("time 1:")

	#this copies the user board and creates a new board
	#user_board = [[0 for i in range(COL)]for j in range(ROW)]
	copy_board = copyBoard(user_board, ROW, COL)
	printBoard(copy_board, ROW, COL)
	printFullBoard(copy_board, ROW, COL)
	
		
	
	
main()

