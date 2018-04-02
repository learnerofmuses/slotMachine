#include <stdio.h>
#include <stdlib.h>       /* for prototype of function rand( ) */

int main( ){


    int i;
    for (i = 1; i <= 20; i++){
        /* pick random number from 1 to 6 and output it */
        printf("%10d", 1 + (rand ( ) %6 ));

        /* if counter is divisible by 5 start new line */
        if (i % 5 == 0 ){

            printf("\n"); 
        } 
    }
    return 0; 


}


