#write a program that generates three 2-D lists
#and for each list the program finds the percent of 0's 
#in the list

import random 

def main():
	row = int(input("enter rows: "))
	col = int(input("enter columns: "))
	
	max_range = int(input("enter max range: "))
	min_range = int(input("enter min range: "))
	
	a = make_2d_list(row, col, max_range, min_range)
	b = make_2d_list(row, col, max_range, min_range)
	c = make_2d_list(row, col, max_range, min_range)
	print(a)
	res = percent(a, row, col, 0)
	if(res==0):
		print(0, "not in the list")
	else:
		print("percent of 0's is", res*100, "%")
	print("\n")
	print(b)
	res = percent(b, row, col, 0)
	if(res==0):
		print(0, "not in the list")
	else:
		print("percent of 0's is", res*100, "%")
	print("\n")
	print(c)
	res = percent(c, row, col, 0)
	if(res==0):
		print(0, "not in the list")
	else:
		print("percent of 0's is", res*100, "%")
	
	
def percent(a, row, col, value):
	c = 0 
	for i in range(row):
		for j in range(col):
			if(a[i][j]==value):
				c+=1
	result = c/(row*col)
	return result 
def make_2d_list(row, col, max_range, min_range):
	a = [[0 for i in range(col)] for j in range(row)]
	for i in range(row):
		for j in range(col):
			a[i][j]=random.randint(min_range, max_range)
	return a
main()
