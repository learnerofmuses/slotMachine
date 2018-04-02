#write a program that randomly generates the list of size 10. Range of 
#the numbers: from -10 to 10. The program creates and prints a new list 
#that contains odd positive vaules only.

import random 

def main():
	my_list = []
	for i in range(10):
		my_list.append(random.randint(-10, 10))
		print("generated list is: ")
		print(my_list)
		odd_positives = oddPos(my_list)
		
		if(len(odd_positives) > 0):
			print("generated list for positives is: ")
			print(oddPos)
		else:
			("no positives")
	return oddPos
main()
