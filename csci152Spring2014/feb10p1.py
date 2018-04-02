#Write a function that has two parameters - list of strings and 
#additional word. The function returns the list of indexes that 
#corresponds to all positions of the word in the string. Example: 
#list=['yana', 'dog', 'yana', 'putty', 'yana', 'yana', 'python', 
#'yana'], word='yana', function will return the following list: 
#[0,2,4,5,7] 

def main():
	size = int(input("enter size of your list: "))
	list_name = []
	for i in range(size):
		name = input("enter name: ")
		list_name.append(name)
	print("list of names ")
	print(list_name)
	name = input("what name are you looking for: ")
	list_index = find_name(list_name, name)
	if(len(list_index)>0):
		print(name, "located on the following positions ")
		print(list_index)
	else:
		print(name, "is not in the list ")


def find_name(lis_name, word):
	list_index = []
	for i in range(len(list_name)):
		if(list_name[i]==word):
			list_index.append(i)
	return list_index
main()	
