        #include <stdio.h> 
        int cube (int x);         /* function prototype */

        int main(){

                int input_num, func_result; 
                printf("please, enter the integer: "); 
                scanf("%d", &input_num);

                func_result = cube (input_num);      /* function call (invokation) */

                printf("The cube of %d is %d\n ", input_num, func_result); 
                return 0; 
        } /* end main function */

        /* definition of the function cube */ 
        /* function cube has one integer parameter and returns the cube of parameter */

        int cube (int x){
                int res; 
                res = x*x*x; 
                return res; 
        }/* end function cube */ 
