#write a function that counts and returns the number of 0's, 1's and 2's 
#in two dimensional list
#complete the main that randomly generates 2-dimenstional list 
#of 0's, 1's and 2's and test your function 


import random

def counter(scores, sizeRow, sizeCol):
	#this function will count the
	#number of 0's, 1's and 2's

	#write your code here	
	count = 0 
	zero = 0 
	one = 0 
	two = 0 
	
	for i in range([i]):
		if(scores =[i][j]):
		


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
	my_list=make_list(my_list, sizeR, sizeC, 2)
	printMatrix(my_list, sizeR, sizeC)
	c0,c1,c2=counter(my_list, sizeR, sizeC)
	print("counters are ")
	if (c0==0):
		print("no 0's in the list ")
	else:
		print("there are ", c0, "0's")
	if (c1==0):
                print("no 0's in the list ")
        else:
                print("there are ", c1, "1's")
	if (c2==0):
                print("no 0's in the list ")
        else:
                print("there are ", c2, "2's")


main()

