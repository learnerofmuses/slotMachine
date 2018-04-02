#write a program that checks if your SSN is prime or not 
#input is a sequence of characters 
#and the output is YES if its prime and NO otherwise 

#xxx-xx-xxxx


def make_dig(my_str):
	new_str=""
	for i in range(len(my_str)):
		if(my_str[i].isdigit()):
			new_str=new_str+my_str[i] 
	return new_str 

def prime(num):
	count=0
	for i in range(1, num+1):
		if(num%i == 0):
			count+=1
	if(count==2):
		return True
	else:
		return False 
	
def main():
	ssn = input("enter your ssn ")
	ssn_str=make_dig(ssn)
	ssn_num = (int)(ssn_str)
	#print(make_dig(ssn))
	if(prime(ssn_num)==True):
		print("your ssn ", ssn, "is prime")
	else:
		print("your ssn", ssn, "is not prime")

main()
