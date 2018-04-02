#Write a program that generates an input configuration into the 
#rectangular board of SizeR rows and SizeC columns. The size of the board 
#could be randomly generated or could be user input. Your program must provide an 
#opportunity to choose. The program calculates the next configurations 
#according to the rules of the Game that were defined above. Your program 
#will be ended if the Game is over or the program calculated 10 (this 
#number make Global Constant) configurations (even if the Game is not over 
#yet). The program has to print the configuration after each step. The 
#program has to print the final statement the statement will notify user 
#that the game is over and state the reason (no change in configuration or 
#10 iterations completed). In both cases, the program will print the number 
#of Live organisms that are on the final board.

import random

def sumNeigh(scores, sizeRow, sizeCol, i, j):
	i = 0
	j = 0  
	sum = scores[i-1][j-1]+scores[i-1][j]+scores[i-1][j+1]
	sum = sum + scores[i][j-1] +scores[i][j+1]
	sum = sum+scores[i+1][j-1]+scores[i+1][j]+scores[i+1][j+1]
	for i in range(sizeRow):
		for j in range(sizeCol):
			if(scores[i][j]==0):
				print([i-1][j-1])
			elif(scores[i][j]==1):
				print([i+1][j+1])			
	return sum, i, j 
	
def make_list(scores, sizeRow, sizeCol, num):
	for i in range(sizeRow):
		for j in range(sizeCol):
			scores[i][j] = random.randint(0, num)
	return scores
def Matrix(scores, sizeRow, sizeCol):
	for i in range(sizeRow):
		print(scores[i])
		
 
def main():
	
	sizeR=int(input("enter size of row "))
	sizeC=int(input("enter size of column "))
	my_list = [[0 for i in range(sizeC)]for j in range(sizeR)]
	num = int(input("enter the range of random numbers "))	
	print Matrix(my_list, sizeR, sizeC)
	

main()
