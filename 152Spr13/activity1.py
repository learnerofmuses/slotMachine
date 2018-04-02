import random 

def randomint_list(size, min_limit, max_limit):
	my_list = []
	for i in range(size):
		n = random.randint(min_limit, max_limit)
		my_list.append(n)
	return my_list

def replace(my_list, item):
	count = 0 
	for i in range(len(my_list)):
		if(my_list[i]%3 == 0):
			count = count + 1
			my_list[i] = item 
	return count

def addFive(a):
	a = a+ 5
	print("in function a= ", a)

def main():
	a = 10 
	print("before function a = ", a)
	addFive(a)
	print("after function a = ", a)
	my_list = randomint_list(10, 1, 100)
	print("list BEFORE function replace is callled")
	print(my_list)
	count = replace(my_list, 0)
	print("AFTER function replace ")
	print(my_list)
	print("function replaced", count, "elements with ", 0)
main()
