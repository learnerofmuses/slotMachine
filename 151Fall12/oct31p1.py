#The chest has 3-digit
#the first digit should be equal to the third digit, the second digit 
#should be even. 
#Write a function openChest that has one parameters, 3-digit positive
#integer. Function checks whether the parameter opens the chest or not
#Function prints YES,if the chest opens and NO otherwise.

#Write a program that reads a sequence of positive
#3-digit integers, first negative or zero terminates an input
#For each integer
#checks
#whether the input
#number opens the chest or not
#You can assume that the input is a 
#positive number between 100 and 999.

def openChest(num):
	digitLast = num%10
	num = num/10
	digitMid = num%10
	num = num/10
	digitFirst = num%10
	if((digitLast==digitFirst) and (digitMid % 2 ==0)):
		print("YES")
	else:
		print("NO")
def main():
	
	num = int(input("enter positive 3-digit integer "))

	while(num > 0):
		openChest(num)
		num = int(input("enter positive 3-digit integer "))

main()
