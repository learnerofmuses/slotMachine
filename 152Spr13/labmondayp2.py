SIZEA = 10
SIZEB = 12
import random

def compare(listA, listB):
	
	countA = 0
	countB = 0 

	for i in range(len(listA)):
	
		if(i%4 == 0 and listA[i]%4 == 0):
			countA = countA + 1
			n = random.randint(1, 100)
	for i in range(len(listB)):
		
		if(i%4 == 0 and listB[i] == 0):
			countB = countB + 1
			n = random.randint(1, 100)
	if(countA > countB):
		res = -1
	
	elif(countA < countB):
		res = 1
	
	else:
		res = 0 
	
	return res

def main():
	n = random.randint(SIZEA)
	n = random.randint(SIZEB)

	print("first list is ")
	print(listA)
	print("second list is ")
	print(listB)

	result = compare(listA, listB)

	if(result == -1):
		print("listA has more odd numbers on positions divisible by 4")
		
	elif(result == 1):
		print("listB has more odd numbers on positions divisible by 4")

	else:
		print("has same amount on positions")

main()
