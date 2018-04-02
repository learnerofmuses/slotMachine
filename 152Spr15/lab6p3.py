#tyler scott
#lab 6 
#problem 3


#Write a function that finds and returns the number of even and number 
#of odd elements in 2-dimensional list, their sums and averages. Write 
#main to test your program. Pay attention, if there are no even elements 
#or no odd element, the first return value will be 0, the sum and 
#average could be any numbers and you would need to use if statemet to 
#print correct results. 

import random 

def list1(my_list, row, col):
	for i in range(row):
		for j in range(col):
			my_list[i][j]=random.randint(0, 11)

def oddList(my_list, row, col):
	odd_list = []
	
	sumO = 0
	
	for i in range(row):
		for j in range(col):
			if(my_list[i][j]%2!=0):
				odd_list.append(my_list[i][j])
	length=len(odd_list)
	for i in range(length):
		sumO=sumO+odd_list[i]
	return sumO, odd_list
def evenList(my_list, row, col):
	even_list = []
	sumE = 0	
	for i in range(row):
		for j in range(col):
			if(my_list[i][j]%2==0):
				even_list.append(my_list[i][j])
	length=len(even_list)
	for i in range(length):
		sumE=sumE+even_list[i]
	return sumE, even_list
def main():
	sizeR=int(input("enter the row size: "))
	sizeC=int(input("enter the column size: "))
	mlist=[[0 for i in range(sizeC)] for j in range(sizeR)]
	list1(mlist, sizeR, sizeC)
	print(mlist)
	sumO, odd_list=oddList(mlist, sizeR, sizeC)
	if(len(odd_list)>0):
		ave=sumO/len(odd_list)
		print(ave)
		print(odd_list)
	else:
		print("no odds")
	sumE, even_list=evenList(mlist, sizeR, sizeC)
	if(len(even_list)>0):
		ave=sumE/len(even_list)
		print(ave)
		print(even_list)
	else:
		print("no evens")
main()
