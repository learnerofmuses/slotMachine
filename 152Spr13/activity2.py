import random 
def randomint_list(size, min_limit, max_limit):
	my_list = []
	for i in range(size):
		n = random.randint(min_limit, max_limit)
		my_list.append(n)
	return my_list 

def removeOdd
