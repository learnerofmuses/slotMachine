
#include<stdio.h>
#include<math.h>

int main(){
	int Seq[22];
	int Bark[22] = {1,0,1,1,0,1,1,1,0,0,0,1,0,1,1,0,1,1,1,0,0,0};
	int Trans[22];
	int Received[22];
	int input;


	printf("Enter in data sequence of 22 0's or 1's\n");
	
	for(int i=0;i<22;i++){
		scanf("%d",&input);
		
		while(input!=0 && input!=1){
			printf("Error. Enter 0 or 1\n");
			scanf("%d",&input);
		}
		Seq[i]=input;
	}
	
	//displays the original sequence
	printf("Here is the given sequence: ");
	//for loop #4.1
	for(int i=0;i<22;i++){
		//if statement 3.1
		if(i!=21){
			printf("%d", Seq[i]);
		}//if 3.1
		else{
			printf("%d\n", Seq[i]);
		}

	for(int i=0;i<22;i++){
		//if statement #0
		if(Seq[i]==Bark[i]){
			Transmitted[i]=0;
		}//if 0
		else{
			Transmitted[i]=1;
		}
	}// for loop #1

	//Transmitting finished
	printf("Transmitted bit(DSSS): ");
	//printf("TESTING %d",Transmitted[0]);printf("%d\n",Trans[1]);
	//for loop #2
	for(int i=0;i<22;i++){
		//if statement 1
		if(i!=21){
			printf("%d", Trans[i]);
		}
		else{
			printf("%d\n", Trans[i]);
		}
	}//for loop #2

	// original dag signal
	printf("Processing the transmitted bit....\n");
	//for loop #3
	for(int i=0;i<22;i++){
		//if statement #2
		if(Trans[i]==Bark[i]){
			Received[i]=0;
		}
		else{
			Received[i]=1;
		}//if 2.E
	}// for loop #3

	//Now to print the sequence which was recieved
	printf("Original sequence: ");
	//for loop #4
	for(int i=0;i<22;i++){
		//if statement #3
		if(i!=21){
			printf("%d", Received[i]);
		}//if 3
		else{
			printf("%d\n", Received[i]);
		}
	} 
}
