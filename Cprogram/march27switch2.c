/*Tyler Scott*/

#include <stdio.h>

int main(){

	    char letter; 
    int aCount = 0,  bCount = 0, cCount = 0, restCount = 0;

    while( (letter = getchar()) != EOF ){

            switch (letter){

                    case 'a': 
                    case 'A':
                             
                             
                            aCount++; 
                            break; 
                    case 'b': 
                    case 'B':
                            bCount++; 
                            break; 
                    case 'c': 
                    case 'C':
                            cCount++; 
                            break; 
                    default:
                            restCount++; 
                            break;

            }
	}
	
    	printf("%d, %d, %d, %d\n ", aCount, bCount, cCount, restCount); 
		
	return 0;
}
