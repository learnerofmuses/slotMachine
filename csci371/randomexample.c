#include <stdlib.h>
#include <time.h>
#include <stdio.h>

int main(){

	srand( (unsigned) (time(0)) ); 
	
	int  i, j;
	int x=1000; 
	int y=2045;
	int count = 0;
	for(i = 0; i < 1000; i++){
		x = rand() % 500;//scaling from 0 - 9
		y = rand() % 200;
		if((x*x + y*y) <= 100.0){
			count+=1;
		} 
	}
	printf("numbers of arrow inside the circle = %d\n", count);

	return 0;
}
