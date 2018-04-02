#Activity 2: Write a function removeOdd
#that has one parameter - list of integers
#function removes the first odd element from the list
#function returns the index of the first odd element in the original list
#if there are NO odd elements in the list, function returns the length of 
#the list which is NOT VALID INDEX

#The program is partially written for you:

#Program randomly generates the list 
#of ints between 1 and 100 of size 10

#complete the program to print the original list BEFORE function removeOdd 
#was called
#call the function removeOdd and print the updated list and the index of 
#the first odd
#element in the original list 


import random
def randomint_list(size, min_limit, max_limit):
        my_list=[]
        for i in range(size):
                n=random.randint(min_limit, max_limit)
                my_list.append(n)
        return my_list

#THIS PART YOU NEED TO WRITE YOURSELF NOW:

def removeOdd(my_list):

	index = len(my_list)
	found=0
        i=0
        while(i<len(my_list) and found == 0):
                if(my_list[i]%2 !=0):
                        item = my_list[i]
                        found=1
			index = i
                i=i+1
        if(found==1):
		my_list.remove(item)
	
	return index


def main():
	my_list=randomint_list(10, 1,100)
	print("Before the function")
	print(my_list)

	index = removeOdd(my_list)
	if(index == len(my_list)):
		print("No odd elements in the list, list remains without change")
	else:
		print("the index of the first odd element is ", index)
		print("the list without first odd element is ")
		print(my_list)	


	#to test the case of NO ODD elements
	#see the code below

	my_list=randomint_list(10, 2,2)
        print("Before the function")
        print(my_list)

        index = removeOdd(my_list)
        if(index == len(my_list)):
                print("No odd elements in the list, list remains without change")
        else:
                print("the index of the first odd element is ", index)
                print("the list without first odd element is ")
                print(my_list)



main()

		

	



