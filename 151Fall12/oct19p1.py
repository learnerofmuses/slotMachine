#write a program that checks the correctness of login and password 
#that user enters

#we will assume that correct login is YANA
#and correct password is ko123

#case sensitive 

#the program must specify if only login is wrong, password is wrong or
#both 

#we will give user 3 times to try 

LOGIN="YANA"
PASSWD="ko123"

def correct(your_login, your_passwd):
	if((your_login==LOGIN) and (your_passwd==PASSWD)):
		print("correct info you can enter your account")
	elif((your_login==LOGIN) and (your_passwd != PASSWD)):
		print("password wrong")
	elif((not(your_login==LOGIN)) and (your_passwd==PASSWD)):
		print("login is wrong")
	else:
		print("login and password are wrong")
def main():
	user_login=input("enter your login ")
	user_passwd=input("enter your passwd ")
	print("the first attempt to login to account results in ")
	correct(user_login, user_passwd)

	user_login=input("enter your login ")
        user_passwd=input("enter your passwd ")
        print("the second attempt to login to account results in ")
        correct(user_login, user_passwd)

	user_login=input("enter your login ")
        user_passwd=input("enter your passwd ")
        print("the third attempt to login to account results in ")
        correct(user_login, user_passwd)

main()

#LAB REPORT
#testing: you must run your program at least 2 times to cover all 4
#choices
#inputs: 'YANA' 'ko123' - correct
#inputs: 'YANA' 'ko1234' - wrong password
#inputs: 'YANA1' 'ko123' - wrong login

