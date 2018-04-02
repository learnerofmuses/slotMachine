def guess(word, letter):
	count = 0
	for i in range(len(word)):
		if(word[i]==letter):
			count = count + 1
			
	return count

def something(my_list, letter):
	m = guess(my_list[0], letter)
	place = 0
	for i in range(1, len(my_list)):
		count = guess(my_list[i], letter)
		if (count > m):
			m = count
			place = i
	return m, place

def main():
	listA=['knicks', 'New York', 'Real madrid', 'basketball', 'soccer']
	letter='k'
	print(something(listA, letter))
	
	
main()






