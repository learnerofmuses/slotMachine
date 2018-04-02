#this program has one parameter - list of grades in the class. the 
#function creates and returns 3 new lists - list of failing grades
#(grades below 60), list of A grades (90 and above) and 
#the rest of the grades (between 60 and 89). 

import random 
SIZE = 15 
MAX = 100 
MIN = 0 

def make_list(size, min_range, max_range): 
	my_list = [] 
	for i in range(size): 
		my_list.append(random.randint(min_range, max_range))
	return my_list 

def separate(my_list):
	fail = [] 
	pass_grade = [] 
	grade_a = [] 

	#if we decide to run the list by index 
	
	for i in range(len(my_list)):
		if(my_list[i] < 60): 
			fail.append(my_list[i])
		elif(my_list[i]>= 60 and my_list[i]<= 89):
			pass_grade.append(my_list[i])
		else: 
			grade_a.append(my_list[i])

	return fail, pass_grade, grade_a

def main(): 
	my_list = make_list(SIZE, MIN, MAX)
	print(my_list)
main()
