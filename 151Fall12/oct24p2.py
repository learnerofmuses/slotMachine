#write a program that finds total number of candy for any number of users
#the number of users it is also an input

#USE TOP DOWN DESIGN 

#if the user enters negative amount the error message will be 
#displayed and that negative amount will be NOT taken toward the total

def totalCandy(users):

	counter = 1
	total = 0
	while(counter <= users):
		userCandy = int(input("enter amount of candy "))
		if(userCandy >=0):
			total = total + userCandy
		else:
			print("ERROR")
		
		counter = counter + 1

	print(total)

def main():
	users = int(input("enter number of users "))
	print("the total number of candy for ", users, " users ")
	totalCandy(users)
main()
