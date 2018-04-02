#write a funtion that converts string to list 
#test it

def main():
	my_str = input("enter sting ")
	my_list = string_to_list(my_str)
	print("my list is ", my_list)

def string_to_list(my_str):
	my_list = []
	for i in range(len(my_str)):
		my_list.append(my_str[i])
	
	return my_list
main()
