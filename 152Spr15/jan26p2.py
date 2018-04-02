#In this program you will perform password validation. A website is 
#publishing the following password rules:
#1. length: at least 6 charachters and no more than 10
#2. the password must include at least ONE special character (the 
#character which is not a letter and not a digit)

#Write a function def valid_pswd(my_str) - that has one parameter, 
#string of characters.
#Function returns True, if my_str is a valid password, and False 
#otherwise

import random 

def random_string(size):
	#starting with empty string
	my_str = ""
	#in the loop we will randomly generate 
	#a number between 33 and 126
	#convert it to character and then add it to the string 
	
	for i in range(size):
		num = random.randint(33, 126)
		#print(num)
		my_str = my_str+chr(num)
	return my_str

def validPsswd(my_str):
	status = False
	length = len(my_str)
	if(length >= 6 and length <=10 and my_str.isalnum()==False):
		status = True
	return status 
		
def main():
	size = random.randint(1, 20)
	my_str = random_string(size)
	print(my_str)
	res = validPsswd(my_str)
	if(res == True):
		print("your password is valid")
	else:
		print("not valid")

main()
