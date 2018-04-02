#include <stdio.h>

int main(void ){

	int x = 25;
	double y = 3.14;
	char z = 'Y';

	printf("CSCI 371 \n");
	printf("Welcome \n");

	printf("enter x, y, z as an integer, float and character:\n");
	scanf("%d", &x);

	printf("enter y as a float:\n");
	scanf("%f", &y);

	printf("enter z as a character:\n");
	scanf("%c", &z);

	printf("x = %d \n", x);
 	printf("y = %f \n", y);
	printf("z = %c \n", z);

	return 0;
}
