#write following functions:
#aveGrade - has two parameters - snumber of students 
#and number of courses for each student
#the function prints the average grade for each student
#2. oddDiv - that has one parameter positive integer
#the function prints the number of off divisors, their sum and average
#3. menu - that has one parameter choice 
#if choice is 1 user will be asked to enter number of 
#students and numbers for courses and aveGrade will called
#if choice is 2 user will be asked to enter integer and 
#function oddDiv will be called
#for other choice function prints error message
#write a main that reads one integer and function menu is 
#called

import random

def aveGrade(nSt, nCo):
	for i in range(nSt):
		sum = 0 
		for j in range(nCo):
			grade = random.randint(1,100)
			print(grade)
			sum = sum + grade
		
		ave = float(sum)/nCo
		print("results for student", i+1) 
		print("student", i+1, "has average", ave)
def oddDiv(num):
	sum = 0 
	count = 0 
	i = 1
	while(i<=num):
		if(num%i == 0) and (i%2 != 0)):
			sum = sum + i
			count = count + 1
		i = i + 1

	if (count>0):
		print("there are ", count, "odd divisors")
		print(their sum is", sum)
		ave = float(sum)/count
		print("their average is", ave)
	else:
		print("no odd divisors")


def menu(choice):
	if(choice == 1):
		print("average grade is in process")
		print("enter number of students")
		nSt=int(input(""))
		print("enter number of courses per student")
		nCo=int(input(""))
		if(nSt>0 and nCo>0):
			aveGrade(nSt, nCo)
		else:
			print("invalid input")
	elif(choice == 2):
		print("odd divisors are in process")
		num = int(input("enter integer "))
		if(num>0):
			oddDiv(num)

		else:
			print("invalid input")
	else:
		print("invalid choice")

def main():
	choice=int(input("enter your choice "))
	menu(choice)
main()	
