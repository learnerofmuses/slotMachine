#puzzle
def main():
	new_list = []
	str=input("enter string: ")
	for i in range(len(str)):
		new_str= str[i:]
		new_list.append(new_str)
	print(new_list)
	print(len(new_list))

main()
