
#include <stdio.h>
#include <stdlib.h>     /* for functions: rand and srand */


int main(){


    int number_to_guess;     /* random number to be guessed. */
    int low_limit;    /* current lower limit of player's range. */
    int high_limit;     /* current upper limit of player's range. */
    int guess_count;     /* Number of times player guessed. */
    int player_number;     /* Number player guessed. */
    int bingo = 0;    /* bingo=0 (false) means user still didn't guess */
                             /* the number, bingo = 1 (true) means user 
guessed the number */

    /* Initialize random number generator. */
    srand(time ( NULL ) );

    /* Not a real pure random number. See restrictions. */
    number_to_guess = rand( ) % 100 + 1;

    /* Initialize variable for loop.*/
    low_limit = 1;
    high_limit = 100;
    guess_count = 1;

    while(!bingo){

        /* Tell user what the bounds are and get his get his guess. */
        printf("Bounds are %d - %d\n ", low_limit , high_limit);
        printf("please enter the next guess guess_ value[ %d ]: ", 
guess_count);
        scanf("%d", &player_number);

        guess_count++;

        /* Did user guess right? */

        if(player_number == number_to_guess){
            bingo = 1; 
        }
        /* Adjust bounds for next guess */
        else if (player_number < number_to_guess)
            low_limit = player_number; else
            high_limit = player_number; 
    }
    printf("Bingo!! You guessed the number within %d times ", guess_count);

    return 0; 


} 
