#Tyler Scott
#Feb 9 2013

#Write a function OddRemove that has one parameter - list of integers. The 
#function counts the number of odd elements, creates a new list that include 
#all odd elements, removes all odd elements from the original list.
#Function returns the counter (the number of odd elements) and the list of 
#odd elements.



def OddRemove(list1):
	list1 = [2, 3, 5, 6, 11, 12, 17, 4, 9, 24]
	new_list = []
	count = 0 
	i = 0
	
	
	for i in range(list1): 
		
		if(list1[i]%2 != 0):
			item = new_list[3]
			count = 1
			new_list.append[i]
		i = i+1			
	if(count==1):
		list1.remove(item)
	return count, new_list	
def main():
	list1 = [2, 3, 5, 6, 11, 12, 17, 4, 9, 24]
	new_list = OddRemove(list1)
	print("List before function")
	print(new_list)
	


main()
	  	

