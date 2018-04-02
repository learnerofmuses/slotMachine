/* Write a program that prompts the user to enter one character. You 
have 
to use switch statement in your program in order to do the following: if 
the input character is 'b', the program reads one number of type double 
and prints this number 5 times on one line, numbers should be separated 
by tab. (you should use loop to do it); if the input character is 'd', 
the program prints the following rectangle:
aaabbb
bbbaaa
aaabbb
bbbaaa
aaabbb
bbbaaa
you have to use loop to do this (TRY TO MAKE IT AS SHORT AS POSSIBLE), 
and if the input character is 'p', the program will find the product of 
all odd numbers between 1 and 15 (including 15) ( you should use loop in 
this part); if the input character is not 'b', 'd' or 'p', the program 
will print the input character 5 times on different lines (you should 
use loop to do it). */ 

#include<stdio.h>

int main(){
	int i=1, prod=1; 
	double num;
	char a; 

	printf("enter a character:\n");
	scanf("%c", &a);
	
	switch(a){

		case 'b':
			printf("enter number:\n");
			scanf("%lf", &num);
			for(i=0; i<=5; i++){
				printf("%f", num);
				printf("\n");
			}
			break;
		case 'd':
			for(i=1; i<=6; i++){
				if(i%2==0){
					printf("bbbaaa\n");
				}
				else{
					printf("aaabb\n");
				}
			}
			break;
		case 'p':
			while(i<=15){
				prod*=i;
				i=i+2;
			}
			printf("product of odds: %d\n", prod);
			break;
		default:
			for(i=0; i<5; i++){
				printf("%c", a);
				print("\n");
				break;
			}
		}
		return 0;		
}
