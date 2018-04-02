#name: Tyler
#date: Nov 12 2012
#Write a program that finds the total amount of candy children collected 
#during Halloween. The program first asks for the number of children and 
#then asks for amount of candy each child collected. When the loop is 
#finished, the program should display the total number of candy collected. 
#Use the following design approach: Write a function that has one 
#parameter - the number of children. The function will read the amount of 
#candy each child collected and output the total amount.
#YOU MUST USE LOOP FOR IN YOUR PROGRAM

def candy (num):
	total = 0

	for i in range(1, num +1):
		userCandy = int(input("enter amount of candy "))
		total = total + userCandy
	  
       	print("amount of candy collected was", total)

       	
             
                	
def main(): 
	num = int(input("enter the number of children "))
	if(num > 0):
		candy(num)
	else:
		print("there was no candy received")
main()
	
	

