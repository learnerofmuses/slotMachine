#Tyler Scott
#ANSWER COMMENTED BELOW

#Test 2 Part 1 (25 points)


#For the program written below, give an example of input to receive the 
#following output

#[5, 0, -15]




def main():
	my_list=[[ 0 for i in range(2)] for j in range(3)]
	fun=[]
	for i in range(3):
		for j in range(2):
			my_list[i][j]=int(input("enter number: "))
			if(my_list[i][j]%5==0):
				fun.append(my_list[i][j])
	print(fun)	
main()	


#INPUT

#enter number: 5
#enter number: 2
#enter number: 0
#enter number: 2
#enter number: 2
#enter number: -15


#OUTPUT

#[5, 0, -15]


