SIZE = 3
def who(num):
	a = 0
	for i in range(SIZE):
		k = num % 10
		a = a + k
		num = num / 10 
	return a

def main():
	n = int(input(""))
	b = 0
	c = 0
	while(n != 0):
		result = who(n)
		print(result)
		b = b + result
		c = c + 1
		n = int(input(""))

	d = float(b)/c
	print(d)

main()
