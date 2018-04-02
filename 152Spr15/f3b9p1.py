#palindrome check

import random 

def palindrome(word):
	rev = reverse_str(word)
	if(rev==word):
		return True
	else:
		return False	

def reverse_str(word):
	rev = ""
	length = len(word)
	for i in range(length-1, -1, -1):
		rev = rev+word[i] 
	return rev 

def reverse_str1(word):
	rev = ""
	length = len(word)
	for i in range(length):
		rev = rev+word[length-1-i]

def main():
	m1 = []
	size=random.randint(5,10)
	print("size of list is ", size)
	for i in range(random.randint(5,10)):
		name = input("enter name ")
		m1.append(name)
	print(m1)
	for i in range(size):
		if(palindrome(m1[i])):
			print(m1[i], "palindrome")
		else:
			print(m1[i], "NOT")
	
main()		
	
