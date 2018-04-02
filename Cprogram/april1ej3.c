        #include <stdio.h> 
        int cube (int x);         /* function prototype */

        int main(){

                int x, i; 
                printf("please, enter the integer: "); 
                scanf("%d", &x); 
                printf("the cubes of all numbers between 0 and %d are\n: " 
, x);

                for (i = 0; i<= x; i++){

                        printf("%d\t", cube(i)); 
                } 
                return 0; 
        } /* end main function */

        /* definition of the function cube */ 
        /* function cube has one integer parameter and returns the cube of 
parameter */

        int cube (int x){
                return x*x*x; 
        }/* end function cube */ 
