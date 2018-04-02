#In this program you will perform password validation. A website is 
#publishing the following password rules:
#1. length: at least 6 charachters and no more than 10
#2. the password must include at least ONE special character (the 
#character which is not a letter and not a digit)

#Write a function def valid_pswd(my_str) - that has one parameter, 
#string of characters.
#Functio returns True, if my_str is a valid password, and False 
#otherwise

#Write a function def valid_list(my_list) which has one parameter, list 
#of strings. Function creates and returns the list of valid passwords 
#Use function valid_ pswd to determine validity of each string in the 
#list. 

#In case and there 
#are no valid passwords, function returns empty 
#list.

#Complete the main to find the list of valid passwords. Make sure you 
#take care of the case of 
#no valid passwords in the list

def main():
	size = int(input("enter size of the list "))
	my_list=[]
	for i in range(size):
		my_str=input("enter string ")
		my_list.append(my_str)
		
	print("original list is ")
	print(my_list)
	
	new_list = valid_pswd(my_str)
	print("valid list is: ")
	print(new_list)

def valid_pswd(my_str):
	pswd = []
	index = 0 
	while index < len(pswd):
		if(my_str == pswd):
			print("true")
		else:
			print("false")
		return true

def valid_list(my_list):
	new_list = []
	new_list = valid_pswd(my_str)	
	if(len(pswd) >=6 and len(pswd) <= 10):
		new_list.append(my_str)

	else:
		print("not valid password")
	return new_list


main()
