
#include <stdio.h>
#define SIZE 15

int main(){
	char word[SIZE];
	int countA=0, countB=0, countC=0, max, min;
	int len, i=0;
	scanf("%s", word);
	printf("%s\n", word); 
	len = strlen(word);
	 
	while(word!='\0'){
		if(word[i]=='a');
			countA++;
		}
		else if(word[i]='b'){
			countB++; 
		}
		else if(word[i]='c'){
			countC++;
		}
		i++;
	}
	
	printf("the value of the letter is... %d\n", count);
	printf("the value of the letter is... %d\n", countA);
	printf("the value of the letter is... %d\n", countB);
	printf("the value of the letter is... %d\n", countC);

	
	if(countA>countB){
		max = countA;
		min = countB;
	}
	else{
		max = countB;
		min = countA;
	}
	if(max<countC){
		max = countC; 
	}
	else{
		max = countC;
		min = countA; 
	}
	if(min>countC){
		max = countB;
		min = countC;
	} 
	else{
		max = countC; 
		min = countB;
	}
	printf(" %d\n", max);
        printf(" %d\n", min);
        printf(" %d\n", countB);
        printf("%d\n", countC);

	return 0;
}
