#name: Tyler
#date: sep 26 

#write a function that has one formal parameter - 4 digit positive 
#integer and prints the average of two middle digits

#write a function that has one formal parameter - 4 digit positive
#integer and prints the average og the first and last digits

#Write a program that ask user to enter THREE 4-digit positive integers 
#and for each number finds the average of the middle digits and the
#average of last digits

def mid_ave(num):
	 
	num = num/10
	d3 = num%10
	num = num/10
	d2 = num%10
	


	print((float(d3+d2))/2)

def end_ave(num):
	d4 = num%10
	num = num/10
	num = num/10
	num = num/10
	d1 = num%10

	print((d1+d4)/float(2))

def main():
	n1 = int(input("enter first int "))
	n2 = int(input("enter second int "))
	n3 = int(input("enter third int "))

	
	print("average of middle digits for each number is ")
	mid_ave(n1)
	mid_ave(n2)
	mid_ave(n3)
	
	print("average of the first and last digits for each number is ")
	end_ave(n1)
	end_ave(n2)
	end_ave(n3)
main()

