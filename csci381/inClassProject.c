/*in class project*/

#include<stdio.h>
#include<math.h>
#define PI 3.1415
int main(){

	double  t, max= 5, incr= 0.1;
	double num;
	for(t=0;t<max;t+=incr){
		num =sin(PI*t);
		printf("\n %f %f" , t, num); 
	}
	return 0;
	}
