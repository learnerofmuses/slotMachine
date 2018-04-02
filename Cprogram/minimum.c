/* March 13 2013

    #include<stdio.h>

    int main(){

            /* declaration of the variables */

            int num1, num2, num3;                 /* input numbers */ 
            int minimum;                         /* minimum among three inputs */

            / * input session */

            printf ("Please enter 3 integers ")             /*user prompt */; 
            scanf("%d%d%d",   &num1, &num2, &num3);        /* input statement that reads thee integers */

            /* find the minimum among the first two numbers */

            if ( num1 < num2 )
                    minimum = num1; 
            else
                    minimum = num2; 

            /* find the minimum among the third number and minimum found so far - final minimum */ 
            if ( num3 < minimum )
                    minimum = num3; 

            /* output the results */ 
            /* outputs the values of the input numbers and the value of the minimum among three inputs  using one printf statement*/

            printf ("the minimum among %d, %d, and %d is %d\n", num1, num2, num3, minimum);

            return 0; 

    } 
