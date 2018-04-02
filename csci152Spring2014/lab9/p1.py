#Write a function def new_string(my_str) that has one parameter - string 
#of characters. The function creates and returns a new string based on 
#the following rules: 1) each lower case letter will be replaced by the 
#correspondent upper case letter 2) each upper case letter will be 
#replaced by the correspondent lower case letter 3) all digits will be 
#removed from the string 4) the rest of the characters will remain 
#without change.

#Example:
#old string: YaNa123&%$
#new modified string: yAnA&%$

#Write main function that reads one string and prints a modified string. 
#Use function new_string to modify the string.

def main():
	my_str = input("enter string: ")
	myString=new_string(my_str)
def new_string(my_str):
	for i in my_str:
		if(i.isupper()):
			myString = i.lower()
			print(myString)
		elif(i.islower()):
			myString = i.upper()
			print(myString)	
		elif(i.isdigit() == False):
			myString = myString+new_string
			print(myString)
main()
