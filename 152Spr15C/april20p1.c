/*write a program that reads a sequence of 10 strings
and finds the number of strings that starts with A or a
*/

#include<stdio.h>
#define SIZE 100 

int countAs();




int main(){
	int result = countAs();
	if(result>0){
		printf("there are %d strings \n", result);
	}
	else{
		printf("no strings started with A or a\n");
	}
	return 0;


}


int countAs(){
	char word[SIZE], fake_char; 
	int i, count=0;
	printf("enter 10 strings:\n");
	for(i=0; i<10; i++){
		scanf("%s", word);
		scanf("%c", &fake_char);
		if(word[0]=='A' || word[0]=='a'){
			count++;
		}
	}
	
	return count;

}
