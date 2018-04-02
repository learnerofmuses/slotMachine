#include <stdio.h>
#include <math.h>

void printValue(double );
void addValue(int, int);

int main(){
	int c, d, e;
	double b;
	printf("enter b: \n");
	scanf("%lf", &b);
	printValue(sqrt(b));

	/*printf("enter c and d:");
	scanf("%d %d", &c, &d);
	e = addValue(c, d);
	printf("e = %d\n", e);
	*/
	return 0;
}

void printValue(double a){
	printf("a = %f\n", a);
}

int addValue(int c, int d){ 
	int e;
	e = c + d;
	return e;
}
