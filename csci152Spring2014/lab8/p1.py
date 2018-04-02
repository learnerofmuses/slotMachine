#In this lab you will write and test the following functions
#1. def build_board_random(row, col) - this function fills the board 
#with random numbers 0 and 1. A live organism is represented by 1 and a 
#dead organism is represented by 0. The sizes of the board will be user 
#input and determine in main 

#2. def build_board_user(row, col) this function fills the board with 
#user input: 0 and 1. A live organism is represented by 1 and a dead 
#organism is represented by 0.

#3.def printBoard(board, row, col) - prints the board (prints 2-d list 
#in matrix form) - we wrote this function already 

#4. def copyBoard(board, row, col) - creates and returns the copy of the 
#board 

#5. def change(oldBoard, newBoard, row, col) - returns 1 if both 2-d 
#lists, oldBoard and newBoard, are the same, and 0 otherwise 

#6. def count(board, row, col) - counts and returns the number of live 
#organisms

#7. def neigh(board, row, col, i, j) - finds and returns the number of 
#live organisms around the cell position i, j 

#8. def all_neigh(board, row, col) - this function creates a 2-d list, 
#with each element equals to the number of live organisms of 2-d list 
#scores. The function returns a new list. 


import random 

def main():
	#this carries out def build board random
	choice = int(input("would you like choice 1 or choice 2: ")) 
	row = int(input("enter the amount of rows: "))
	col = int(input("enter the amount of columns: "))
	buildU = build_board_user(row, col)
	buildR = build_board_random(row, col)
	
	if(choice == 1):
		make_new_board(oldBoard, row, col)
	elif(choice == 2):
		make_new_board(oldBoard, row, col)
def make_new_board(oldBoard, row, col):
		a = [[ 0 for i in range(col)] for j in range(row)]
		for i in range(row):
			for j in range(col):
				newBoard = neigh(scores, sizeRow, sizeCol, i, j)
		return newBoard				
def build_board_random(row, col):
	
	a = [[ 0 for i in range(col)] for j in range(row)] 

	for i in range(row):
		for j in range(col):
  			a[i][j] = random.randint(0,1)
	return a

def build_board_user(row, col): 
        a = [[0 for i in range(col)] for j in range(row)]
        for i in range(row):
                for j in range(col):
                        a[i][j] = int(input("enter 0: "))
        return a

def printBoard(board, row, col):
	for i in range(row):
		print(board[i])
	
def copyBoard(board, row, col):
	a = [[0 for i in range(col)] for j in range(row)]
	for i in range(row):
		for j in range(col):
			a[i][j]= board[i][j]
	return a

def change(oldBoard, newBoard, row, col):	
	change = 0 
	for i in range(row):
		for j in range(col):
			if(oldBoard[i][j] == newBoard[i][j]):
				change +=1
		
	if(change == row*col):
		return 1
	else:
		return 0

def count(board, row, col):
	liveOrg = 0
	for i in range(row):
		for j in range(col):
			if(board[i][j] == 1):
				liveOrg +=1
			 
	return liveOrg

def neigh(scores, sizeRow, sizeCol, i, j):

	sum=0

        #Center
	if(i>0 and j>0 and i<sizeRow-1 and j<sizeCol-1):
        	sum=scores[i-1][j-1]+scores[i-1][j]+scores[i-1][j+1]
        	sum=sum+scores[i][j-1]+scores[i][j+1]
        	sum=sum+scores[i+1][j-1]+scores[i+1][j]+scores[i+1][j+1]

        #Top Left Corner
	elif(i==0 and j==0):
		sum=scores[i][j+1]+scores[i+1][j+1]+scores[i+1][j]

        #Bottom Left Corner
	elif(j==0 and i==sizeRow-1):
                sum=scores[i-1][j]+scores[i][j+1]+scores[i-1][j+1]

        #Top Right Corner
	elif(i==0 and j==sizeCol-1):
		sum=scores[i][j-1]+scores[i+1][j]+scores[i+1][j-1]

        #Bottom Right Corner
	elif(i==sizeRow-1 and j==sizeCol-1):
		sum=scores[i][j-1]+scores[i-1][j]+scores[i-1][j-1]

        #Left Border
	elif(j==0 and i>0 and i<sizeRow-1):
		sum=scores[i+1][j]+scores[i-1][j]+scores[i][j+1]
		sum=sum+scores[i+1][j+1]+scores[i-1][j+1]

        #Top Border
	elif(i==0 and j>0 and j<sizeCol-1):
		sum=scores[i][j-1]+scores[i][j+1]+scores[i+1][j]+score[i+1][j+1]+score[i+1][j-1]
	
	#Right Border
	elif(j==sizeCol-1 and i>0 and i<sizeRow-1):
		sum=scores[i-1][j]+scores[i+1][j]+scores[i][j-1]
		sum=sum+scores[i-1][j-1]+scores[i+1][j-1]

        #Bottom Border
	elif(i==sizeRow-1 and j>0 and j<sizeCol-1):
        	sum=scores[i][j-1]+scores[i][j+1]+scores[i-1][j]
        	sum=sum+scores[i-1][j-1]+scores[i-1][j+1]

	return sum



def all_neigh(scores, sizeRow, sizeCol):

	list = [[ 0 for i in range(sizeCol)] for j in range(sizeRow)]
	for i in range(sizeRow):
		for j in range(sizeCol):
			list[i][j]=neigh(scores, sizeRow, sizeCol, i, j)
	return list


main()
