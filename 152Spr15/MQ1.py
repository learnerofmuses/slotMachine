#Tyler Scott
#MINI QUIZ 1

#Write a function: def separate(grades)

#that has one parameter - list of grades in the class. The function 
#creates and RETURNS 3 new lists - list of failing grades (grades below 
#60), list of A grades (90 and above) and the rest of the grades 
#(between 60 and 89).

#Write a program that randomly generates the list of grades of size 15, 
#calls function separate, and then prints THREE lists: failing grades, 
#list of A grades, and the rest of the grades.

SIZE = 15
import random 

def main():
	my_list = [0]*SIZE
	for i in range(SIZE):
		my_list[i]=random.randint(0,100)
	
	num,num1,num2=separate(my_list)
	print("original list is:")
	print(my_list)
	print("list of failing grades is:")
	print(num)
	print("list of passing grades is:")
	print(num1)
	print("list of A grades are:")
	print(num2)
	
	
def separate(grades):
	 
	a = 0
	b = 0
	c = 0
	for i in range(SIZE):
		if(grades[i]>=0 and grades[i]<=59):
                	a+=1
		if(grades[i]>=60 and grades[i]<=89):
                	b+=1
		if(grades[i]>=90 and grades[i]<=100):
			c+=1

	num = [0]*a
	num1 = [0]*b
	num2 = [0]*c
	a=0
	b=0
	c=0
	for i in range(SIZE):
		if(grades[i]>=0 and grades[i]<=59):
			num[a]=grades[i]
			a+=1
			
		if(grades[i]>=60 and grades[i]<=89):
			num1[b]=grades[i]
			b+=1
		
		if(grades[i]>=90 and grades[i]<=100):
			num2[c]=grades[i]
			c+=1
	print("number of failing grades:", a)
	print("number of passing grades:", b)
	print("number of A grades:", c)		
	return num, num1, num2 

main()	
