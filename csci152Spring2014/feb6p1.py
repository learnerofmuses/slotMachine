#Design a program that asks the user to enter a series
#of 20 numbers. The program should store the numbers in a list 
#and then display the following data:

#the lowest number in the list
#the highest number in the list
#the total of the number in the list 
#the average of the numbers in the list 

import random 

def deadpool(my_list):
	sum = 0 
	average = 0
	count = 0 
	while(count<0):	
		

def main():
	size = random.randint(20)
	my_list = []
	
	for i in range(size):
		my_list.append(random.randint(1, 100))

	print("generated list is: ")
	print(my_list)

	if(len(my_list)>0):
		print
