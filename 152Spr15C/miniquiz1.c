/*Vitamin D is an important vitamin. The following table shows serum 
concentrations of the Vitamin D and correspondent health status:*/ 

#include<stdio.h>

int main(){

	int a;
	int vD;
	int D;
	int A;
	int oD;
	int d_lvl;
	int i = 0; 
	printf("how many  people came to lab for vitamin D test\n");
	scanf("%d", &a);
	
	printf("what is the vitamin D level\n");
	scanf("%d", &d_lvl);

	printf("people with very deficient health\n", vD);
	scanf("%d", &vD);
	printf("people with  deficeint health\n", D);
	scanf("%d", &D); 
	printf("people with adequate health\n", A);
	scanf("%d", &A);
	printf("people with overdose health\n", oD);
	scanf("%d", &oD);
	
	return 0;

	while(i<a){
	
	/*printf("what is the vitamin D  level");*/
	scanf("%d", &d_lvl);
	
	if(d_lvl <=11){
		i+=d_lvl;
		vD++;
	}
	else if(d_lvl>=12 && d_lvl <=19){
		i+=d_lvl;
		D++;
	}
	else if(d_lvl>=20 && d_lvl <=49){
		i+=d_lvl;
		A++;
		
	}
	else if (d_lvl >=50){
		i+=d_lvl;
		oD++;
	}
	}	
 
}
