/* Tyler Scott
/* March 11 2013

/* My second C program is Addition Program
input: two integers
output: sum of two integers */

#include <stdio.h>

/* function main begins program execution*/

int main()
{

    int num1;    /* first number to be input by user */ 
    int num2;   /* second number to be input by user */ 
    int sum;    /* variable in which sum will be stored */

    printf ( "enter first integer\n" );   /* prompt */ 
    scanf ( "%d", &num1 );             /* read an integer */

    printf ( "enter second integer\n" );   /* prompt */ 
    scanf ( "%d", &num2 );                 /* read an integer */

    sum = num1 + num2;   /* assign total to sum */

    printf ( "Sum is %d\n", sum );   /* print sum */

    return 0;

    } 
