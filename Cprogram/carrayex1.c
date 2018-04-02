    #include<stdio.h>

    int main(){

            int num[5];      /* num is an array of 5 integers*/ 
            int i;

            printf("Please enter 5 integers - elements of the array "); 
            for (i = 0; i < 5; i++){
                    scanf("%d", &num[i]); 
            } 
            printf("Elements of the array are: \n"); 
            for (i = 0; i < 5; i++){
                    printf("the element %d is %d \n", i, num[i]); 
            }

            return 0; 

    } 
