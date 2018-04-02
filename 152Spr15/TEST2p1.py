#Tyler Scott
#ANSWER COMMENTED BELOW 

#TEST 2 PART 1 

#FOR THE PROGRAM WRITTEN BELOW, GIVE AN EXAMPLE OF INPUT TO RECEIVE THE 
#FOLLOWING OUTPUT 

#[5, 0, -15] 


def main():
	my_list=[[0 for i in range(2)] for j in range(3)] 
	fun = []
	for i in range(3):
		for j in range(2):
			my_list[i][j]=int(input("enter a number: "))
			if(my_list[i][j]%5==0):
				fun.append(my_list[i][j])
	print(fun)

main()


#INPUT 1 

#enter a number: 5
#enter a number: 2
#enter a number: 0
#enter a number: 2
#enter a number: 2
#enter a number: -15 

#OUTPUT 1

#[5, 0, -15]

#INPUT 2

#enter a number: 2
#enter a number: 5
#enter a number: 0
#enter a number: 2
#enter a number: 2 
#enter a number: -15

#OUTPUT 2

#[5, 0, -15]

#INPUT 3 

#enter a number: 5
#enter a number: 3
#enter a number: 3
#enter a number: 0
#enter a number: -15
#enter a number: 4

#OUTPUT 3

#[5, 0, -15]
