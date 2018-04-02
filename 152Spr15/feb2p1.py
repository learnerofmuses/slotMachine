#write a program that validates the password 
#the rules are: length at least 8 chars
#no longer than 12, at least one upper case
#at least one lower case, at least one digit 
#and at least one special chars, but you are not allowed
#to use % and !


import random 
MAX=15  
MIN=7

def make_str(min, max):
	size = random.randint(min, max)
	mstr=''
	for i in range(size):
		n = random.randint(33, 126)
		mstr=mstr+chr(n)

	return mstr

def valid(mstr):
#conditions/rules
	up = False 
	low = False
	length = False 
	di = False 
	special = False 
	#calculate if len_mstr = length 
	len_mstr=len(mstr)
	if(len_mstr>=8 and len_mstr<=12):
		length=True 

	#checking for at least one uppercase character	
	for i in range(len_mstr):
		if(mstr[i].isupper()==True):
			up=True
	#checking for at least one lowercase character
		elif(mstr[i].islower()==True):
			low=True
	#checking for at least one digit
		elif(mstr[i].isdigit()==True):
			di=True
	#checking for at least one special character expect % and !
		elif(not(mstr[i].isalnum())):
			special=True
	if('%' in mstr):
		special=False
	if('!' in mstr):
		special=False

	if(length and up and low and di and special):
	#or if (length==True and up==True and low==True and di==True and special==True):
		return True
	else: 
		return False
def main():
	psswd=make_str(MIN, MAX)
	print(psswd)
	val=valid(psswd)
	counter=1
	while(val==False):
		psswd=make_str(MIN, MAX)
		print(psswd)
		val=valid(psswd)
		counter+=1
	print("the valid password is ", psswd)
	print("it took", counter, "steps")
main()
