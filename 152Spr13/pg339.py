#Tyler Scott
#Feb 6 2013


def compare(my_list):
	a = 0
	a1 = 0 
	new = []
	new1 = []	

	for i in range(len(my_list)):
		n = input("choose answer: A, B, C, D: ")
    		if n in my_list[i]:   
			a = a + 1          
		else:
			a1 = a1 + 1
			new.append(n)
		new.append(n)
	if(a > 15):
		res = "You have passed!"

	else: 
		res = "You have failed, sorry"

	return res, a, a1, new, new1


	
def main():
	my_list = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']
	res, X, Y, Z, new = compare(my_list)
	print("the answer is", res)
	print("the answers are")
	print(my_list)
	print("the correct number of answers is", X)
	print("You have passed!")
	print("the wrong number of answers you have are", Y)
	print("the number of answers are", Z)
	
	

main() 	

