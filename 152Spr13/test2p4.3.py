#Write a function countValue that accepts FOUR parameters: 
#two-dimensional list of integers, sizeR and sizeC (sizes of the list) and 
#the additional integer. 
#The function returns the amount of times that integer appears in the list. 

#Write a function maxList that accepts FOUR parameters: 
#TWO two-dimensional lists of integers (assume that both lists has the same 
#size), and the sizes of the lists ? sizeR and sizeC. The function randomly 
#generates integer between 1 and 100. 
#The function counts the number of times this integer appears in each 
#list. Use function countValue to perform this task. The function returns the 
#list with the maximal amount of appearances. 


def countValue(my_list, sizeR, sizeC, num):
	count = 0 
	for i in range(sizeR):
		for j in range(sizeC):
			if(my_list[i][j] == num):
				count = count + 1
	return count 

	
