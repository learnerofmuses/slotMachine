    #include<stdio.h> 
    #include<stdlib.h> 
    #include<time.h> 
    #define SIZE 7

    int main(){

            int frequency[SIZE] = {0}; /* all counters have initial value 0 */ 
            int face; /* random value between 1 and 6 */ 
            int roll; /* total amount of rolls */ 
            int i;

            srand(time(NULL)); /* seed random-number generator */

            for (roll = 1; roll <= 6000; roll++){
                    face = 1 + rand ( )% 6; 
                    frequency[face]++; 
            }

            printf("%s%17s\n", "Face", "Frequency");

            for (face = 1; face < SIZE; face++){
                    printf("%4d%17d\n", face, frequency[ face ]); 
            }

            return 0; 

    } 
