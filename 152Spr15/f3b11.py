#write a program that reads a sequence of strings 
#the program will change each string in the following way
#lower case letters will be replaced by the corresponding upper case
#letters and all digits will be replaced by *, and * chars will 
#be removed 

#YanAKo123*
#yANakO***

def string_change(mstr):
	new=""
	length=len(mstr)
	for i in range(length):
		if(mstr[i].islower()):
			new=new+mstr[i].upper()
		elif(mstr[i].isupper()):
			new=new+mstr[i].lower()

		elif(mstr[i].isdigit()):
			new=new+"*"
		elif(mstr[i]!="*"):
			new=new+mstr[i]
	return new

def list_change(ml):
	nlist=[]
	length=len(ml)
	for i in range(length):
		new_element=string_change(ml[i])
		nlist.append(new_element)
	return nlist
def main():
	size=int(input("enter size of the list: "))
	ml=[]
	for i in range(size):
		ml.append(input("enter string: "))
	print("original list: ")
	print(ml)
	nlist = list_change(ml)
	print("new_list: ")
	print(nlist)

main()
