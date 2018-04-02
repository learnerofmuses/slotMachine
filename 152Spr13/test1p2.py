LENGTH = 8 
def guess(listA, listB, size):
	new = []
	count = 0 
	for i in range(size):
		if(listA[i]  != listB[i]):
			count = count+1
			new.append(listA[i])
	return new, count 

def main():
	listA = ['a', 'B', 'c', 'D', 'k', 'K', 'P', 'o']
	listB = ['f', 'B', 'o', 'D', 'k', 'L', 'P', 'b']
	new, count = guess(listA, listB, LENGTH)
	if(count > 0):
		print(new, count)
	else:
		print("lists are the same")
main()
