#Write a program that randomly generates the 2-dimensional list. Make 
#sizes of the list user input. Program prints the list in 3 different 
#ways: all elements on different rows, each row on separate line, and 
#list form ([[ first row], [second row]...[..]] 


import random 

def main():
	row = int(input("enter rows: "))
	col = int(input("enter columns: "))
	a = [[ 0 for i in range(col)] for j in range(row)] 
	for i in range(row):
		for j in range(col):
			a[i][j]= random.randint(0, 10)	
			print a[i][j]

	for i in range(row):
		print a[i]
	print a

main()	
