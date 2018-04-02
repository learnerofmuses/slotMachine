#Write a function count_letter that has one parameter - string. The 
#function counts and returns the number of lowercase letters in the 
#string and the number of uppercase letters in the string. Write main 
#that reads one string and calls the function count_letter to find and 
#print the number of lowercase and uppercase letters in the input 
#string. 

def count_letter(my_str):
	lowcount = 0
	uPcount = 0 
	
	for i in my_str:
		if(my_str[i].islower()):
			lowcount = 1
		elif(my_str[i].isupper()):
			uPcount = 1
	return lowcount, uPcount

def main():
	string_1 = input("enter string: ")
	lowcount, uPcount = count_letter(string_1)

	print("there are", lowcount, "lowercase letters ")
	print("there are", uPcount, "uppercase letters ")


main()
