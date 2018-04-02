#include<stdio.h>
#include<math.h>
int main(){

        int n;             /* Input number tested. */ 
        int divisor = 2;       /* First possible divisor tested. */ 
        int max_divisor;       /* Largest divisor tested. */ 
        int prime = 1;       /* 1 (means true) if n prime, 0 (means false) 
otherwise. */

        /* Read input */ 
        printf("Please enter a non-negative number "); 
        scanf("%d", &n);

        if (n <= 1)       /* Check for n<=1. */
                prime = 0;       /* n = 1 or n = 0 not prime numbers */ 
        else if (n>2){

                max_divisor = (int)( sqrt( n ) + 0.5 );

                /* check all divisors up to max_divisor. Stop when a 
divisor is found. */ 
                while ( ( divisor <= max_divisor ) && ( prime ) ){
                        if (n % divisor == 0)
                                prime = 0; 
                        divisor ++; 
                } 
        }



