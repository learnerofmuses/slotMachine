#a. Write a function def rev(my_str) which has one parameter, a string of characters. 
#The function creates and returns a new string which is a reverse of my_str. For 
#example, if my_str is yana this function returns anay, and if my_str is bony, the 
#function returns ynob 

#b. Write a function rev_list(my_list) which has one parameter - list of strings. The 
#function creates a new list using the following rule: each string in the list will be 
#replaced by reverse string. Use function rev to reverse each individual string. For 
#example, if my_list is ["yana", "bob", "bony", "I"] the function returns the 
#following list: ["anay", "bob", "ynob", "I"] 

#c. Write main function that asks user to enter size of the list and then asks user 
#to enter appropriate number of strings to creare a list of strings. Then call 
#function rev_list to reverse all string in the list, and then finds the number of 
#strings that remained the same after reverse operation. For example, if user entered 
#5 for the size, and the following strings: ["yana", "bob", "I", "madam", "ada"], the 
#reverse strings will be: ["anay", "bob", "I", "madam", "ada"] and the program will 
#print "there are 3 strings that reads the same in forward and reverse direction". 


def main():
	my_str = input("enter string:")
	newString=rev(my_str)
	print(newString)
	
def rev(my_list):
	newlist = [] 
	for j in range(len(my_list[-1:])):
		my_str= ''
		
		my_str = my_str+my_list
		newlist.append(my_str)
	return newlist
	
main()
