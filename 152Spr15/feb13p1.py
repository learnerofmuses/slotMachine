#lab 5 
#program #3

def compare(str1, str2):

	len1=len(str1)
	len2=len(str2)
	
	match = 0 
	if(len!=len2):
		match = -1
	else:
		for i in range(len1):
			if(str1[i]==str2[i]):
				match+=1
	return match 

def make_list(size):
	ml=[]
	for i in range(size):
		ml.append(input("enter string: "))
	return ml 
def main():
	size = int(input("enter size: "))
	print("enter first list")
	ml1=make_list(size)
	ml2=make_list(size)
	for i in range(size):
		match=compare(ml1[i], ml2[i])
		if(match==-1):
			print(ml1[i], "and", ml2[i], "not the same length")
		else:
			print(ml1[i], "and", ml2[i], "has", match, "matches") 


main()
