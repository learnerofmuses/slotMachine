#Tyler Scott
#TEST 2 PART 2

#Write a function valid_license that has 1 parameter -  
#string of characters that represents license plate. 
#The function returns True if the license plate is valid and False 
#otherwise

#The rules of valid license plate:
#1. the license plate is at least 4 characters long 
#and no more than 7 characters long
#2. the license plate consists of digits and letters only. 

#Write a function count_valid, that has one parameter -
#list of license plates
#The function finds and returns the number of 
#valid licenses in the list and the new list
#that consists of valid lincenses ONLY

#Write main that reads the size of the list, generates the list of 
#licenses from user input and finds the 
#number of valid licenses in the list and prints all valid 
#licenses 

def valid_license(plate):
	valid = ""
	status = False
	length = len(plate)
	if(length >= 4 and length <= 7 and plate.isalnum()==True):
		
		status = True
		
	return status

def count_valid(my_list):
	count = 0
	size = len(my_list) 
	for i in range(0, size):
		isValid=valid_license(my_list[i])
		if(isValid==True):
			count+=1
			
		
	new_list = []
	for i in range(0, size):
		#print("looking at", my_list[i])
		isValid=valid_license(my_list[i])
		if(isValid==True):
			#print("this license plate is valid")
			new_list.append(my_list[i])
		#else:
			#print("this is not valid")

		
	return count, new_list
		
	
def main():
	
	size=int(input("enter the number of plates in the list: "))
	my_list=[]
	for i in range(size):
		plate = (input("enter the plate: "))
		my_list.append(plate)
		#valid_license(plate)
	print("original list is: ")
	print(my_list)
	
	count,validlist=count_valid(my_list)
	print("amount valid", count)
	print("this is new list", validlist)
	
main() 
