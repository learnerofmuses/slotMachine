/*Tyler Scott*/

#include <stdio.h>

int main(){

	    char letter; 
    int uppercase, lowercase; 
    int value; 
    letter = getchar(); /* function getchar() reads one character from the keyboard */

    switch (letter){

            case 'a': 
            case 'A':
                    uppercase = 'A'; 
                    lowercase = 'a'; 
                    printf("%d, %d", uppercase, lowercase); 
                    break; 
            case 'b': 
            case 'B':
                    value = letter; 
                    printf("the ASCII value of the character %c is %d", letter, value); 
                    break; 
            case 'c': 
            case 'C':
                    printf("%d", letter); 
                    break; 
            default:
                    printf ("Illegal letter!\n"); 
                    break; 
	
    } 
	return 0;
}
