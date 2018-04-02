#write a program that randomly generates the list 
#of integers between -10 and 10 of size (10-20)
#your program will create 3 new lists
#one that holds only POSITIVE, one that only holds NEGATIVES, 	
#and one that holds only ZEROSs

#write a separate function that haves one parameter
#original list and returns 3 NEW lists

import random 

def main():
	size = random.randint(10, 20)
	print("size =", size)
	my_list= []
	for i in range(size):
		my_list.append(random.randint(-10, 10))
		
	print("generated list is ")	
	print(my_list)
	
	pos_list, neg_list, zero_list = separate(my_list)

	if(len(pos_list)>0):

		print("generated list for positives is: ")
		print(pos_list)
	else:
		("no positives")

	print("generated list for negatives is: ")
	print(neg_list)
	if(len(zero_list)>0):

		print("generated list for zeros is: ")
		print(zero_list)
	else:
		print("no zeros")

def separate(my_list):
	pos = []
	neg = []
	zero = []
	
	for i in my_list:
		if(i>0):
			pos.append(i)
		elif(i<0):
			neg.append(i)
		else:
			zero.append(i)
	
	return pos, neg, zero
	
main()
