/* monday lab pr 2 */

#include<string.h>
#include<stdio.h>
#define SIZE 100 

void changeString(char old_array[], char new_array[]);


int main(){
	char old_array[SIZE], new_array[SIZE];
	printf("enter string: \n");
	scanf("%s", old_array);
	changeString(old_array, new_array);
	if(strlen(new_array)==0){
		printf("nothing left\n");
	}
	else{ 
		printf("new string is: %s\n", new_array);
	}
	return 0; 

}

void changeString(char old_array[], char new_array[]){
	int i=0, j=0;


	
	
	while(old_array[i]!='\0'){
		if(old_array[i]>='0' && old_array[i]<='9'){
			new_array[j]='*';
			j++;
		}
		else if(old_array[i]>='a' && old_array[i]<='z'){
			new_array[j]=old_array[i];
			j++;
		}
		else if(old_array[i]>='A' && old_array[i]<='Z'){
			new_array[j]=old_array[i];
			j++;
		}
		i++;
	}
	new_array[j]='\0';
}

