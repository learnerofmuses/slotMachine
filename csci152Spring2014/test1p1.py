def guess(my_list, num):
	count = 0
	new=[]
	
	for i in my_list:
		if(i == num):
			count = count+1
			new.append(i)
	return count,  new

def main():
	my_list = [0]*5
	for i in range(5):
		my_list[i]=int(input("enter list element "))
	num_to_look = int(input("enter integer "))
	count, new = guess(my_list, num_to_look)
	if (count > 0):
		print(count, new)

	else:
		print(num_to_look, "not in the list ")


main()


