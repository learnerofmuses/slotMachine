#name: Tyler 
#date: sep 19 
#write the program that reads 3 positive integers
#the program finds
#1. sum of the inputs
#2. average of the inputs
#3. average of the last digits of the inputs 


#example:
#input: 1003 16 157 
#output:
#sum = 1176
#average = 392.0
#averageLastDigits = (3+6+7)/3.0 = 16/3. = 5.3333

#output results with 3 decimal digits after decimal point 

#Part I: Input

num1 = int(input("enter first positive int "))
num2 = int(input("enter first positive int "))
num3 = int(input("enter first positive int "))

#Part II: Calculations

sum = num1 + num2 + num3
average = float(sum)/3

#to calculate the last digit of the number
#apply % 10


LDigit1 = num1 % 10 
LDigit2 = num2 % 10 
LDigit3 = num3 % 10 


sumLastDigits = LDigit1 + LDigit2 + LDigit3
aveLastDig = sumLastDigits/float(3)


#Part III: Results


print("sum of inputs is ")
print(sum)
print("average of inputs is ")
print(format(average, '.3f'))
print("sum of lastdigits is ")
print(sumLastDigits)
print("average of last digits is ")
print(format(aveLastDig, '.3f'))

 
