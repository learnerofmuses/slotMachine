#include <stdio.h>
#include <stdlib.h>       /* for rand and srand functions */

int main( ){

    int i;
    srand( time (NULL) ); /* use computer clock to get a seed value */
    for (i = 1; i <= 20; i++){
        /* pick random number from 1 to 100 and output it */
        printf("%10d", 1 + (rand ( ) % 100 ));

        /* if counter is divisible by 5 start new line */
        if (i % 5 == 0 ){

            printf("\n"); 
        } 
    }
    return 0; 


} 
