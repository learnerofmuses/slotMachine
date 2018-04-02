#Write a program that randomly generates the 2-dimensional list. Make 
#sizes of the list user input. Program prints all odd elements. 

import random 

def main():

	row = int(input("enter number of rows: "))
	col = int(input("enter number of cols: "))
	odd = []
	a = [[0 for i in range(col)] for j in range(row)]
	for i in range(row):
		for j in range(col):
			a[i][j]= random.randint(0, 15)
	print a					
	for i in range(row):
		for j in range(col):
			if(a[i][j]%2 != 0):
				print(a[i][j])
				odd.append(a[i][j])
	
	if(len(odd)==0):
		print("no odd numbers")
	else:
		print("odd numbers")
	print(odd)
main()
