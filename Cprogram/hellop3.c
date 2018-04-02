/* Tyler Scott
/* March 11 2013

#include <stdio.h>

/*function main begins program execution*/

int main()
{

int num1; /*first number to be input by user*/
int num2; /*second number to be input by user*/
int num3; /*third number to be input by user*/
int sum; /*variable in which sum will be stored*/
int product; /*variable in which product will be stored*/

printf("enter first integer\n"); /*prompt */
scanf( "%d", &num1); /*read an integer */
	
printf("enter second integer\n"); /*prompt */
scanf( "%d", &num2); /*read an integer */

printf("enter third integer\n"); /*prompt */
scanf( "%d", &num3); /*read an integer */

sum = num1 + num2 + num3; /*assign total to sum */
printf("Sum is %d\n", sum); /*print sum*/
	
product = num1 * num2 * num3; /*assign total to product */
printf("Product is %d\n", product); /*print product*/

return 0;
}
