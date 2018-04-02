/*Write a function int sumASCII(char s[]) that finds the sum of 
the ASCII values of the elements of the array s. Write a C 
program that reads a string (use function stringInput that we 
wrote in class) and finds the sum of the ASCII values of the 
elements using function sumASCII. Define the size of array using 
#define statement.*/

#include<stdio.h>
#define SIZE 100

int sumASCII(char s[]);

int main(){
	char word[SIZE];
	int sum; 
	scanf("%s", word);
	sum=sumASCII(word); 
	printf("the sum of the ASCII value is %d", sum);
	return 0; 

} 


int sumASCII(char s[]){
	int i = 0, sum = 0;
	while(s[i]!='\0'){
 		
		sum+=(int)s[i];
		i++;
	}
	return sum;
}
