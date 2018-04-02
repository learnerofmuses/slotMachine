#name: Tyler
#date: sep 24
#write a program that reads 3 positive integers
#the program will find 
#1. the sum of the inputs
#2. average of the inputs
#3. average of the last digits of the inputs

#Part I: Input

num1 = int(input("enter first positive int "))
num2 = int(input("enter second positive int "))
num3 = int(input("enter third positive int "))

#Part II: Calculations

sum = num1 + num2 + num3 
average = float(sum)/3

#to calculate the last digit of the number
#apply % 10

LDigit1 = num1 % 10 
LDigit2 = num2 % 10 
LDigit3 = num3 % 10 

sumLastDigits = LDigit1 + LDigit2 + LDigit3
aveLastDigits = sumLastDigits/float(3)

#Part III: Results

print("sum of inputs is ")
print(sum)
print("average of inputs is ")
print("sum of last digits is ")
print(sumLastDigits)
  
