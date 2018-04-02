#write a program that randomly generates 
#2-D list of ints range -10, 10
#assume that the number or rows and number columns 
#is the same 
#program creates one dimensional list of ALL items
#from 2-D list and additional one dimensional list 
#that include only DIAGONAL elements
#then program removes all diagonal elements of the 1-D
#list

import random 

def main():
	size = int(input("enter size of 2-d list "))
	my_list2d = make_2d_list(size, size)
	print("my 2-d list is\n ")
	print(my_list2d)
	print("\n2-d list in matrix form")
	for i in range(size):
		print(my_list2d[i])
	print("\nPrinting one dimensional list \n")

	choice = random.randint(0,1)
	print("choice = ", choice)
	if (choice==1):
		my_list1d=convert1(my_list2d, size, size)
		print(my_list1d)
	else:
		my_list1d=convert(my_list2d, size, size)
		print(my_list1d)
	diag = make_diag(my_list2d, size, size)
	print("\ndiagonal list is\n ")
	print(diag)
	
	
def remove_diag(a_1d, diag):
	for i in diag:
		a_1d.remove(i)
	#another solution:
	#for i in range(len(diag)):
		#a_1d.remove(diag[i])

def make_2d_list(row, col):
	a = [[0 for i in range(col)] for j in range(row)]
	for i in range(row):
		for j in range(col):
			a[i][j]=random.randint(-10, 10)
	return a

def convert(a_2d, row, col):
	a_1d = []
	for i in range(row):
		for j in range(col):
			a_1d.append(a_2d[i][j])
	return a_1d

def convert1(a_2d, row, col):
	#we will declare 1-d list in different way
	a_1d=[0]*(row*col)
	k = 0 
	for i in range(row):
		for j in range(col):
			a_1d[k] = a_2d[i][j]
			k+=1
			
	return a_1d

def make_diag(a_2d, row, col):
	diag = [] 
	for i in range(row):
		diag.append(a_2d[i][j])
	return diag

def make_diag1(a_2d, row, col):
	diag = []
	for i in range(col):
		if(i==j):
			diag.append(a2d[i][j]
	return diag
main()
