#write a program that will ask 7 users to enter the amount of candy
#they got for Halloween and find the total amount for all 7 users

def main():
	counter = 1
	total = 0
	
	while(counter<=7):
		userCandy = int(input("enter amount of candy "))
		
		total = total + userCandy
		counter = counter + 1
	print("the total number of candy for 7 users is ")
	print(total)
main()
