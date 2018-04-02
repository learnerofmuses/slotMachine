#In this program you will perfrom password validation. A website is
#publication the following password rules:
#1. length: at least 6 characters and no more than 10 
#2. the password must include at least ONE special character
#(the character which is not a letter and not a digit)

import random 

def random_string(size):
	my_str = ""

	for i in range(size):
		num = random.randint(33, 126)
		#print(num)
		my_str = my_str+chr(num)
	
	return my_str

def validPsswd(my_str):
	status = False 
	length = len(my_str)
	if(length >= 6 and length <= 10 and my_str.isalnum()==False):
		status = True 
	return status


main
