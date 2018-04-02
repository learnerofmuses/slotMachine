
LENGTH = 5
def guess(listA, listB, size):
	new=[]
	count = 0
	for i in range(size):
		if(listA[i] != listB[i]):
			count = count + 1
			new.append(listA[i])
	return new, count

def main():
	listA=[0]*LENGTH
	listB=[0]*LENGTH
	for i in range(LENGTH):
		listA[i]=int(input("enter element for list A "))
	for i in range(LENGTH):
                listB[i]=int(input("enter element for list B "))

	new, count = guess(listA, listB, LENGTH)
	if (count > 0):
		print(new, count)

	else:
		print("special case")


main()


