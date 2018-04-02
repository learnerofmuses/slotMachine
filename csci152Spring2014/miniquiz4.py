#Write a function def process(my_string), that has one parameter - 
#string of characters. The function counts the number of upper case 
#letters, lower case letters, and the digits. The counters will be 
#stored in one dimensional list of integers. Function returns the one 
#dimensional list of counters. Write a program that inputs one string, 
#then calls function process to find the counters, and then finds which 
#category has the most characters (Try to do this WITHOUT IF statement). 

def main():
	user = int(input("enter a string: "))
	process(my_string)
	
def process(my_string):
	Ucount = 0 
	Lcount = 0 
	Dcount = 0 
	my_list = []
	if(user.upper()):
		print("uppercase letters")
		my_list.append(user.upper())
		return Ucount
	else:
		print("no uppercase letters")
	if(user.lower()):
		print("lowercase letters")
		my_list.append(user.lower())
		return Lcount
	else:
		print("no lowercase letters")
	if(user.isdigit()):
		print("digits only")
		my_list.append(user.isdigits())
		return Dcount
	else:
		print("no digits")

main()
			
