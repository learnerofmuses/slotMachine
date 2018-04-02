#tyler scott
#lab 6
#problem 2

#Write a program that randomly generates the 2-dimensional list. Make 
#sizes of the list user input. Program prints all odd elements, finds 
#the number of odd elements, their average and sum. Make a 
#one-dimensional list of all odd elements. Have a separate function that 
#counts odd elements. Use the return value, counter, to decide on 
#calling function average and sum. Only if there are odd elements, you 
#can calculate the average and sum. 

import random 

def list1(my_list, row, col):
	for i in range(row):
		for j in range(col):
			my_list[i][j]=random.randint(0, 15)
	return my_list

def oddList(my_list):
	odd_list = []
	sumO = 0
	for i in range(row):
		for i in range(col):
			if(my_list[i][j]%2!=0):
				odd_list.append(my_list[i][j])
		length=len(odd_list)
		for i in range(length):
			sumO, odd_list[i]
		return sumO, odd_list
def main():
	sizeR=int(input("enter the row size: "))
	sizeC=int(input("enter the column size: "))
	mlist=[[0 for i in range(sizeC)]for j in range(sizeR)]	
	list1(mlist, sizeR, sizeC)
	print(mlist)
	sumO, odd_list=oddList(mlist)
	if(len(odd_list)>0):
		ave=sumO/len(odd_list)
		print(ave)
		print(odd_list)
	else:
		print("no odds")	
	
main()
