    #include<stdio.h > 
    int main(){

            int n;        /* Input number. */ 
            int divisor;     /* Possible divisor tested. */ 
            int counter = 0;     /* Number of divisors found. */

            /* Read input */ 
            printf( "Please enter a number "); 
            scanf("%d", &n);

            /* Check and count all possible divisors. */ 
            for (divisor = 1; divisor <= n; divisor ++){
                    if (n % divisor == 0)
                            counter ++; 
            }

            /* Print output */ 
            if (counter == 2)
                    printf("The number %d is a prime number \n", n); 
            else
                    printf("The number %d is not a prime number\n", n);

            return 0; 

    } 
