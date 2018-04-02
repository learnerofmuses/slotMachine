#write a function dig_div_3 that has one parameter 
#string of chars and it returns the number of digits divisible by 3 
#string = 718247^#&^827kdsksk
#function returns: 0
#string = 139&*(*(^@!#$*^(
#return: 2

#write a program that creates a list of strings of input size 
#and for each string finds the number of digits div by 3 
#and average number of digits div by 3 

def dig_div_3(mstr):
	counter = 0 
	for i in range(len(mstr)):
		if(mstr[i].isdigit() and ((int)(mstr[i]))%3==0):
			counter+=1
	return counter

def list_dig_div3(ml):
	length=len(ml)
	sum=0
	new_list=[] 
	for i in range(length):
		res=dig_div_3(ml[i])
		new_list.append(res)
		if(res==0):
			print("no digits divisible by 3")
		else:
			print(res, "digits divisible by 3")
		
		sum=sum+res
	ave=sum/length
	return ave, new_list

def main():
	size=int(input("enter size: ")
	ml=[]
	for i in range(size):
		ml.append(input("enter string: "))
	ave, new_list=list_dig_div3(ml)
	print(ave)
	print(new_list)
main()
