#include <stdio.h>
#include <stdlib.h>       /* for rand and srand functions */

int main( ){

    int i;
    unsigned seed; /* number used to seed the random number generator */
    printf("Enter the seed: ");
    scanf("%u", &seed);
    srand(seed); /* seed the random number generator */

    for (i = 1; i <= 20; i++){
        /* pick random number from 4 to 10 and output it */
        printf("%10d", 4 + (rand ( ) % 7 ));

        /* if counter is divisible by 5 start new line */
        if (i % 5 == 0 ){

            printf("\n"); 
        } 
    }
    return 0; 


} 
