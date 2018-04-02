#write a program that reads list of strings
#and creates a new list with each word rotated 90 degrees
#assume all words are same length 


def main():
	list = ["yana", "bony", "cold", "snow"]
	new_str=new_list(list)
	print(new_str)
def new_list(my_list):
	newlist=[]
	for j in range(len(my_list[0])):
	
		my_str= ''
		for i in range(len(my_list)):
			my_str=my_str+my_list[i][j]
		newlist.append(my_str)
	return newlist
						
	

main()
