#Write a function that has one parameter - list of integers and returns 
#the number of positive elements, negative elemens and zeros 

import random 

def main():
	size = random.randint(0, 20)
	if(size!=0):
		result_list = make_list(size)
		print(result_list)
		cP, cN, cZ = process(result_list)
		if(cP != 0):
			print("there are", cP, "positives"
		else:
			print("no positives")
		if(cN > 0):
			print("there are", cN, "negatives")
		else:
			print("there are no negatives")
		if(cZ> 0):
			print("there are", cZ, "zeros")
		else:
			print("there are no zeros")
	
def make_list(size):
	my_list = []
	for i in range(size):
		my_list.append(random.randint(-100, 100))
	return my_list
#different way to generate list
#my_list = [0]*size
#for i in range(size):
#	my_list[i] = random.randint(-100, 100)
#return my_list
def process(my_list):
	cPos = 0
	cNeg = 0 
	cZero = 0
	for i in range(len(my_list)):
		if(my_list[i] > 0):
			cPos +=1
		elif(m_list[i] < 0):
			cNeg +=1
		else:
			cZero +=1
	return cPos, cNeg, cZero
	
main()
	
