#write a program that reads 5 grades and creates a list
#finds sum and average of the grades

N=5
def main():
	grades=[0]*N
	print("GRADES AT THE BEGINNING")
	print(grades)
	i=0
	sum=0
	print("enter ", N, "grades")
	while(i<len(grades)):
		grades[i]=int(input())
		sum=sum+grades[i]
		i=i+1

	print(grades)
	print("sum of the grades is ", sum)
	print("the average of the grades is ",float(sum)/N)
main()
