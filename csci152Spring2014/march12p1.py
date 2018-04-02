#write a program that asks for number of users
#and then first name, last name, and student ID for each student
#and creates a login for each student using the following rule:
#login = first 3 letters of the first name, first 2 letters of 
#the last name, and last 3 digits of the student ID
#if the name is less than 3 characters we will pad the rest of
#characters with letter z (the same rule for last name)


def main():
	size = int(input("enter size of the class "))
	for i in range(size):
		f = input('first name: ')
		l = input('last name: ')
		id = input('ID: ')
		your_login = make_login(f, l, id)
		print("your login is: ", your_login)

def make_login(first, last, ID):
	login = ""
	if(len(first) >=3):
		login = login+first[0:3]
	elif(len(first) == 2):
		login = login+first+'z'
	else:
		login = login+first+'zz'

	if(len(last) >=2):
		login = login+last[0:2]
	else:
		login = login+last+'z'
	
	login = login+ID[-3:]
	
	return login 
main()
