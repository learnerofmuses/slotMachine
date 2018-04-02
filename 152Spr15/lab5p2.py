#Tyler Scott
#Feb 11, 2015
#Lab 5 problem 2


#Write a function change that has one parameter - string of 
#characters. 
#The function removes all digits from the original string and returns 
#the new string without any digits. Pay attention: since Python cannot 
#change the original string, you need to create a new string and copy 
#all non-digit chars from the original string to the new one and then 
#return a new string.

#Write a program that generates the list of strings and for each string 
#removes all its digits. The program prints updated listed at the end 


def change(m_str):
	new = "" 
	string = len(m_str)
	for i in range(string):
		if(m_str[i].isdigit()):
			new+= m_str[i] 	
		elif(m_str[i].isdigit()):
			new = ""
		else:
			new+= m_str[i]		
	return new
def list(ml):
	nlist=[]
	length=len(ml)
	for i in range(length):
		nE = change(ml[i])
		nlist.append(nE)
	return nlist
def main():
	size = 1
	mstr = [] 
	for i in range(size):	
		mstr.append(input("enter string: "))
	print("original string: ")
	print(mstr)
	nlist = change(mstr) 
	print("new string: ")
	print(nlist)

main()
	
