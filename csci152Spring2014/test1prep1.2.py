def guess(my_list):
	count = 0
	sum = 0
	new=[]
	
	for i in my_list:
		if(i%3 == 0):
			count = count+1
			sum = sum + i
			new.append(i)
			
	if(count==0):
		average = -1
		sum = - 1
	else:
		average = float(sum)/count
	
	return sum, average, new
	
def something(my_list):
	index_new=[]
	for i in range(len(my_list)):
		if (my_list[i] %2 !=0 ):
			index_new.append(i)
	return index_new

def word_index(my_list, word):
	index_new=[]
	for i in range(len(my_list)):
                if (my_list[i] == word ):
                        index_new.append(i)
        return index_new
def main():
	print("part I")
	my_list = [3, 9, 10, 12, 1, 7, 5, 27]
	sum, average, new = guess(my_list)
	print(sum, average, new)
	
	print("part II")
	my_list=[1, 2, 4, 7, 11]
	sum, average, new = guess(my_list)
	print(sum, average, new)
	
	print("part III")
	my_list = [3, 9, 10, 12, 1, 7, 5, 27, 14, 18]
	index_new=something(my_list)
	
	len_new=len(index_new)
	if (len_new>0):
		print(index_new)
		print(my_list)
		odd_list=[]
        	for i in index_new:
                	odd_list.append(my_list[i])
        	print(odd_list)
		
		for i in odd_list:
			
			my_list.remove(i)
		print(my_list)
	else:
		print("index list is emprty ")
		
	print("part 4")
	my_list=['yana', 'dog', 'yana', 'putty', 'yana', 'yana', 
'python', 'yana']
	word='yana'
	index_new=word_index(my_list,word)
	print(index_new)

main()	


