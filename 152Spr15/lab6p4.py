#tyler scott
#lab 6
#problem 4

#Write a function that finds and returns the number of elements that are 
#divisible by 3. Function also creates and returns the new 
#ONE-DIMENSIONAL list that includes all elements that are divisible by 
#3. Write main to test your program 


import random 

def make_list(my_list, row, col):
	for i in range(row):
		for j in range(col):
			my_list[i][j]=random.randint(0,15)
	return my_list

def div3(my_list, row, col):
	list=[]
	for i in range(row):
		for j in range(col):
			if(my_list[i][j]%3==0):
				list.append(my_list[i][j])
	return list
def main():
	sizeR=int(input("enter rows: "))
	sizeC=int(input("enter columns: "))
	mlist=[[0 for i in range(sizeC)] for j in range(sizeR)]
	mlist=make_list(mlist, sizeR, sizeC)
	print(mlist)
	d = div3(mlist, sizeR, sizeC)
	print(d)
		
	
main()
