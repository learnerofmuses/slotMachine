#include <stdio.h>
void product (int a, int b); /* function prototype */

int main(){

    int i, m;
    scanf("%d", &m);
    for (i = 1; i <= m; i++){

        product (i, m);
        printf("\n"); 
    }
    return 0; 


}

/* function definition */
void product (int a, int b){

    int i;
    for (i = 1; i <= b; i++){

        printf("%d\t", a*i); 
    } 


}


