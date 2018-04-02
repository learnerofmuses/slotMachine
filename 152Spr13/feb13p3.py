#write a function that counts and returns the number of appearances of 
each element in two-dimensional list 
#use additional one-dimensional list that will store the counter values
#look on the example we did in class 
#http://cs.widener.edu/~yanako/html/courses/Spring13/csci152/game.txt
#click on February 4 examples Dice Game Using List of Counters 
 


import random

	

def counterEfficient(scores, sizeRow, sizeCol, size):
	count =  size + 1 
	for i in range(sizeRow):
		for j in range(sizeCol):
			new_list = [i][j]= random.randint(



def make_list(scores, sizeRow, sizeCol, num):
	for i in range(sizeRow):
		for j in range(sizeCol):
			
			scores[i][j]=random.randint(0,num)
	return scores

def printMatrix(scores, sizeRow, sizeCol):
        for i in range(sizeRow):
                print(scores[i])

def main():
	sizeR=int(input("enter row size "))
	sizeC=int(input("enter column size "))
	my_list =[[0 for i in range(sizeC)]for j in range(sizeR)]
	num=int(input("enter the range of random numbers")) 
	my_list=make_list(my_list, sizeR, sizeC, num)
	printMatrix(my_list, sizeR, sizeC)

	
main()

