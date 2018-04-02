/* Write a program that first reads one integer. 
If the FIRST integer is 1 the program reads a sequence of NEGATIVE 
integers. First POSITIVE or ZERO  integer will terminate the input. The 
program 
finds and prints the average of the inputs that are divisible by 5, their 
sum and amount.
If the FIRST integer is 2, the program reads 1 positive integer and finds 
if the integer is PRIME or NOT. Prime number is a number that has only 2 
divisors: 1 and the number itself

If the FIRST input is not 1, or 2, the program prints error message.

 */

#include<stdio.h>

int main(){
	
	int choice, num, sum = 0, counter = 0, divisor;
	double average;

	printf("enter choice, 1 or 2 \n");

	scanf("%d", &choice);

	if (choice == 1){
		printf("enter sequence of NEGATIVE ints\n");
		scanf("%d", &num);	
		while (num < 0){
			if(num % 5 ==0){
				counter++;
				sum+=num;
			}
			scanf("%d", &num);
		}


		/*PAY ATTENTION AVERAGE MUST BE CALCULATED AFTER THE LOOP 
*/
		if(counter > 0){
			average = (double)(sum)/counter;
	
			/* all results must be printed INSIDE THIS IF */
			printf("there are %d nums divisible by 5\n", 
counter);
			printf("their sum is %d\n", sum);
			printf("their average is %f\n", average);
		}
		else{
			printf("no div by 5 \n");
		}
	}
	else if(choice == 2){
		printf("enter positive integer\n");
		scanf("%d", &num);
		if(num > 0){

			counter  = 0;
			for (divisor=1; divisor<=num; divisor++){
				if(num%divisor == 0){
					counter++;
				}
			}
			if(counter == 2){
				printf("%d is prime\n", num);
			}
			else{
				printf("%d is NOT prime\n", num);
                        }

		}
		else{
			printf("INVALID INPUT\n");
               }

	}
	else{
		printf("INVALID CHOICE\n");
        }


	return 0;
}

