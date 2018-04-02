#problem 2 
#write a function that has one parameter - list of integers and returns 
#the average of the elements with the EVEN index. Write a main to test 
#your function. 


def aveEvenInd(my_list):
	sum = 0 
	c = 0
	for i in range(len(my_list)):
		if(i%2==0):
			sum = sum+my_list[i]
			c+=1
	if(c!= 0):
		return sum/c

def main():
	my_list = [2, 3, -9, 3, 4, -10, 5, 16] 
	res = aveEvenInd(my_list)
	if(res !=none):
		print("average is ", res)
	else:
		print("no elements on even index")
	
	my_list1 = []
	res = aveEvenInd(my_list) 
	if(res !=none):
        	print("average is ", res)
	else:
        	print("no elements on even index")


main() 
