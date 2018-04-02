    #include <stdio.h>

    /* Function prototypes */ 
    void Menu(void); 
    float TriangleArea(float width, float height); 
    int isdigit(char ch); 
    int fibonacci(int n);

    int main(){

            Menu(); 
            return 0; 

    }

    /* Menu: A menu for testing our functions 
    Parameters: none. 
    Returns: no return value. 
    Algorithm: trivial. */ 
    void Menu(void){

            int finish = 0; /* Exit from menu. */ 
            int choice ; /* User's choice from menu.*/ 
            float width; /* Width of triangle. */ 
            float height; /* Height of triangle. */ 
            char ch; /* charcter (for isdigit) */ 
            int n; /* serial fibonaci number (for fibonacci) */

            while (!finish){ 
            printf("Menu:\n " ); 
            printf(" 1) triangle Area.\n"); 
            printf(" 2) isdigit.\n"); 
            printf(" 3) fibonaci.\n"); 
            printf(" 0) exit.\n"); 
            printf("Enter your choice: "); 
            scanf("%d", &choice);
	    
            switch (choice){ 
            case 0:
                    finish = 1; 
                    break; 
            case 1:
                    printf("Enter width and height of triangle "); 
                    scanf("%f%f", &width, &height); 
                    printf("Area of triangle = %f", TriangleArea(width, height)); 
                    break; 
            case 2:
		    ch=getchar();
                    printf("Enter a character "); 
                    ch = getchar( ); 
                    if (isdigit(ch))
                            printf("%c is digit\n ", ch); 
                    else
                            printf("%c is not digit ", ch); 
                    break; 
            case 3:
                    printf("Enter n "); 
                    scanf("%d", &n); 
                    printf("The %d -th fibonaci number is %d\n", n, 
fibonacci (n)); 
                    break; 
            default:
                    printf("Illegal Choice! Try Again.\n"); 
                    break; 
            } 
	    }
    }
     
    /* fibonacci: Finds n'th Fibonacci number. 
    Parameters: n (input parameter). 
    Returns: n'th Fibonacci number. 
    Algorithm: Iterative, using the formula f(n) = f(n - 1) + f(n - 2), n 
>= 2 
    f(0) = f(1) = 1 */

    int fibonacci(int n){

            int f_prev = 1; /* f( n - 1 ) (initialized to f(1) = 1) */ 
            int f_prev_prev = 1; /* f( n - 2 ) (initialized to f(0) = 1) 
*/ 
            int f_current; /* f( n ) */ 
            int counter; // counts number of iterations.

            if ( n <= 1 ){
                    f_current = 1; 
            } 
            else{
                    for (counter = 2; counter <= n; counter ++){
                            f_current = f_prev + f_prev_prev; 
                            f_prev_prev = f_prev; 
                            f_prev = f_current; 
                    } 
            } 
            return (f_current); 

    }

    int isdigit(char ch){

            int res; 
            if (((ch >= '0') && (ch <= '9')))
                    res = 1; 
            else
                    res = 0; 
            return res; 

    } 
    /* function definition 
    function TriangleArea: Comutes the area of triangle 
    Parameters: width - width of triangle (input parameter) 
    height - height of triangle (input parameter) 
    Returns: The area of a triangle. */

    float TriangleArea(float width, float height){

            float area; //area of triangle 
            area = width*height/2.0; 
            return area; 

    } 
