#write a loop that counts the number of digits that appear in the string referenced by mystring 
 
def main():
	
	my_str = input("enter a string: ")
	myString=new_string(my_str)
	print(myString)
def new_string(my_str):
	countD  = 1 
	for i in my_str:
		if(i.isdigit()):
			myString = myString+new_string
			countD = countD + i.digit()
	return countD				
		
main()
