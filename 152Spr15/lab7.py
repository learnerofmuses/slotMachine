#In this lab you will write and test the following functions

#1. def build_board_random(row, col) - this function fills the board with 
#random numbers 0 and 1. A live organism is represented by 1 and a dead 
#organism is represented by 0. The sizes of the board will be user 
#input and determine in main

#2. def build_board_user(row, col) this function fills the board with 
#user input: 0 and 1. A live organism is represented by 1 and a dead 
#organism is represented by 0.

#3. def printBoard(board, row, col) - prints the board (prints 2-d list 
#in matrix form) - we wrote this function already

#4. def copyBoard(board, row, col) - creates and returns the copy of the 
#board

#5. def change(oldBoard, newBoard, row, col) - returns 1 if both 2-d 
#lists, oldBoard and newBoard, are the same, and 0 otherwise

#6. def count(board, row, col) - counts and returns the number of live 
#organisms

#7.def neigh(board, row, col, i, j) - finds and returns the number of 
#live organisms around the cell position i, j

#8.def all_neigh(board, row, col) - this function creates a 2-d list, 
#with each element equals to the number of live organisms of 2-d list 
#scores. The function returns a new list.


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
	new_board=[[0 for i in range (col+2)]for j in range (row+2)]
	for i in range(row+2):
		for j in range(col+2):
			new_board[i][j]=board[i][j]
	print("copied board: ")
	return new_board
def change(oldBoard, newBoard, row, col):
	count = 0
	for i in range(1, row+1):
		for j in range(1, col+1):
			if(oldBoard[i][j]==newBoard[i][j]):
				count+=1			
	if(count == (row*col)):
		res = 1
	else:
		res = 0
	return res 	
#def count(board, row, col):
#	lives = 0 
#	for i in range(1, row+1):
#		for j in range(1, col+1):
#			if(board[i][j]==1):
#				lives+=1
#		return lives

#def neigh(board, row, col, i, j):
#	count = board[i-1][j]+board[i+1][j]+board[i][j-1]+board[i][j+1]
#	count = count+board[i-1][j-1]+board[i-1][j+1]+board[i+1][j-1]+board[i+1][j+1]
#	return count 
#def all_neigh(board, row, col):
#	neigh_board=[[0 for i in range (col+2)]for j in range (row+2)]
#	for i in range(1, row+1):
#		for j in range(1, col+1):
#			neigh_board=neigh[i][j](board, row, col, i, j)
#	return neigh_board

def main():
	#this prints the random board
	print("random board: ")
	board = build_board_random(ROW, COL)
	print(board)

	#this prints the user made board
	user_board = [[0 for i in range(COL)]for j in range(ROW)]
	user_board = build_board_user(ROW, COL)
	print(user_board)

	#this prints board and full board
	printBoard(board, ROW, COL)
	printFullBoard(board, ROW, COL)

	#this copies the user board and creates a new board
	new_board = copyBoard(board, ROW, COL)
	printBoard(board, ROW, COL)
	printFullBoard(board, ROW, COL)

	print(new_board)
	
	#this changes the board
	res=change(oldBoard, newBoard, ROW, COL)
	printBoard(board, ROW, COL)
	printFullBoard(board, ROW, COL)
	print("here is the changed board: ")
	print(changed_board)
	
main()
