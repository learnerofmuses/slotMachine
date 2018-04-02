/* wednesday lab pr 2 */

#include<string.h>
#include<stdio.h>
#define SIZE 100

void changeString(char oldA[], char newA[]);

int main(){

        char oldA[SIZE], newA[SIZE];
        printf("enter string: \n");
        scanf("%s", oldA);
        changeString(oldA, newA); 
        if(strlen(newA)==0){
                printf("nothing left\n");
        }
        else{
                printf("the new string is: %s\n", newA);
        }
        return 0;
}

void changeString(char oldA[], char newA[]){
        int i=0, j=0; 

        while(oldA[i]!='\0'){
                if(oldA[i]>='0' && oldA[i]<='9'){
                        newA[j]=oldA[i];
                        j++;
                }
                else if(oldA[i]>='a' && oldA[i]<='z'){
                        newA[j]='*';
                        j++;
		}
                else if(oldA[i]<='A'  && oldA[i]<='Z'){
                        newA[j]=oldA[i];
                        j++;
                else if(oldA[i]>='[' && oldA[i]<='*'){
                        newA[j]=oldA[i];
                }
                else if(oldA[i]>='(' && oldA<='-'){
                        newA[j]=oldA[i];
                }
                i++;
        }
        newA[j]='\0';
}



