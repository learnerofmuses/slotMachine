#name: Tyler
#date: Nov 5 2012
#Write a program that first reads one integer. If the integer is EVEN, the program reads 7 real 
#numbers. Each number indicates the distance in miles the person travel in one day. The program 
#finds and prints the average distance in kilometers for these 7 days. Use the following formula 
#to convert miles to kilometers: km = miles * 1.609344

#If the integer is ODD, the program reads 7 real numbers. Each number indicates the distance in 
#kilometers the person travel in one day. The program finds and prints the average distance in 
#miles for these 7 days. 
#Use the following formula to convert kilometers to miles: miles = km * 0.6214 

def MtoKm(period):
	total = 0 
	count = 1
	
	print("enter ", period, "miles ")
	while(period<= miles):
	
		num = float(input(" "))
	if(num % 2 == 0) and (num % 4 == 0): 
		total = total + num 
		count = count + 1
	aveM = float(total)/period
	aveKm = aveM * 1.609344
	print("average kilometers is ", aveKm)

def check(choice):
	(choice % 2 == 0)
       	period = int(input("enter period of times in days "))
	MtoKm(period)
def main():
	choice = int(input("enter choice "))
	check(choice)
main()
		
