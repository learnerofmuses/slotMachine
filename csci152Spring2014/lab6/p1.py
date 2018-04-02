#In this program you will perform some statistical analysis of the 
#grades in some course. Write a program that first asks user
#to enter the number of students in the class.
#The the program asks user to enter the grade for each student in class.
#The results are stored in the list of integers. Assume that the input 
#is valid. The program must find the following (write separate function 
#for each task):
#Average grade in the class

#Highest grade in the class, the number of students who received 
#highest grade, and their positions in the list of grades(must be done 
#in ONE function, with 3 return value.)

def main():
	average()
	
def average():
	n = int(input("enter number of students in class: "))
	my_list = []
	sum = 0
        for i in range(n):
        	num = int(input("what is your grade?: "))
       		my_list.append(num)
		
		sum += num
	average = sum/n
	print("the average grade of the class was:")
	print(average)
	print("the highest grade in the class was:")
	print(max(my_list))
def highest(my_list, item):
	
	item_index = my_list.index(num)
	sort(my_list)
	c = 0
	for i in my_list:
		if(i==item):
			c+=1
	if(num <= 100 and num >= 90):
		print(max(my_list))
	elif(num <= 89 and num >= 80):
		print(max(my_list))
	elif(num <= 79 and num >= 70):
		print(max(my_list))
	elif(num <= 69 and num >= 60):
		print(max(my_list))
	elif(num <= 59 and num >= 0):
		print(max(my_list))
	
	return c, item_index, my_list.sort	

main()
	
