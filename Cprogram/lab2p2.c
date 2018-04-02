/*Tyler Scott
March 20 2013
There is a treasure box with 1 million dollars. The chest has a 3-digit 
combination lock that opens under the following conditions: the first 
digit should be equal to the last digit, the second digit should be even, 
and the sum of all digits should be divisible by 4. Write a program that 
reads ONE 3-digits integer between 100 and 999. The program checks if the 
input number opens the chest or not. The output should be YES, if the 
chest opens, and NO otherwise. Check validity of the input and output the 
error message in case of invalid input.

You can do the loop version and write a program that reads a series of 
non-negative integers between 100 and 999. The first negative value will 
terminate the input. For each input, the program checks if the number 
opens the chest or not. For each input, the output should be YES, if the 
chest opens, and NO otherwise.

Examples: Inputs: 525 425 515 505
Outputs:
YES NO NO NO*/

#include <stdio.h>

int main(){
	
	int num;
	int d1, d2, d3;
	int sum = 0;

	printf("enter your 3 digit integer\n");
	scanf("%d", &num);
	while(num>0){
	if(num >= 100 && num <= 999){
		d3 = num%10;
		num = num/10;	
		d2 = num%10;
		num = num/10;
		d1 = num%10;
		sum = d1+d2+d3;
		
		 if(d1 == d3 && d2 % 2 == 0 && sum % 4 == 0){		
			printf("YES\n");
		}
		else{
			printf("NO\n");
		}
		
	}
	else{
		printf("invalid input\n");
	}
	scanf("%d", &num);
	} 
	return 0;
	
}
