#write a program the randomly generates 
#2-d list of random sizes
#and finds number of even elements and their sum and average

import random 
def main():
	row = random.randint(3,5)
	col = random.randint(3,5)
	my_list = [[ 0 for i in range(col)] for j in range(row)]
	print(my_list)
	for i in range(col):
		my_list[i][j] = random.randint(-5, 5)
	
	print("\nmy list is:", my_list)
	cE = 0
	sum = 0
	for i in range(col):
		if(my_list[i][j]%2 == 0):
			cE +=1
			sum+= my_list[i][j]
	if(cE > 0):
		print("sum is ", sum)
		print("average is ", sum/cE)
	else:
		print("no evens")

main()
