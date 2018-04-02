#write a function that counts and returns the number of 0's, 1's and 2's 
#in two dimensional list
#complete the main that randomly generates 2-dimenstional list 
#of 0's, 1's and 2's and test your function 


import random
def better_counter(scores, sizeRow, sizeCol):
	counter = [0]*3
	for i in range(sizeRow):
		for j in range(sizeCol):
			counter[scores[i][j]]+=1
	return counter
def counter(scores, sizeRow, sizeCol):
	#this function will count the
	#number of 0's, 1's and 2's

	#write your code here	
	c0=0
	c1=0
	c2=0
	for i in range(sizeRow):
		for j in range(sizeCol):
			if(scores[i][j]==0):
				c0+=1
			elif(scores[i][j]==1):
				c1+=1
			elif(scores[i][j]==2):
				c2+=1
		return c0, c1, c2



def make_list(scores, sizeRow, sizeCol, num):
	for i in range(sizeRow):
		for j in range(sizeCol):
			
			scores[i][j]=random.randint(0,num)
	return scores

def printMatrix(scores, sizeRow, sizeCol):
        for i in range(sizeRow):
                print(scores[i])

def main():
	sizeR=int(input("enter row size: "))
	sizeC=int(input("enter column size: "))
	my_list =[[0 for i in range(sizeC)]for j in range(sizeR)] 
	my_list=make_list(my_list, sizeR, sizeC, 2)
	printMatrix(my_list, sizeR, sizeC)
	c0, c1, c2=counter(my_list, sizeR, sizeC)
	print("counters are", c0,c1,c2)
	count=better_counter(my_list, sizeR, sizeC)
	print(count)
	#complete the main

main()

