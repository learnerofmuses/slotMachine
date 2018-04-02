#include <stdio.h>
void printStar (int num); /* function prototype */

int main(){

    int i, m;
    scanf("%d", &m);	
    for (i = 1; i <= m; i++){

        printStar ( i );
        printf("\n"); 
    }
    return 0; 


}

/* function definition */
void printStar (int num){

    int i;
    for (i = 1; i <= num; i++){

        printf("*"); 
    } 


} 
