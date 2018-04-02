#include<stdio.h>
#include<math.h>

int score(int numJudges);
int main(){
	int Nsong, numJudges, i = 2, songScore, WiN; 
	double winner, songScore;
	printf("enter the number of songs\n");
	scanf("%d", &Nsong);
	printf("enter number of judges:\n ");
	scanf("%d", &numJudges);
	printf("what is the score for this song?:\n");
	winner = score(numJudges);
	winScore=1;
	printf("song 1: %d," winner);
	for(i=2; i< numJudges; i++){
		printf("enter the score for the next song:\n");
		songScore=score(numJudges);
		printf("song %d, %.2f\n",WiN, songScore);
		if(songScore > winner){
			winner = songScore;
			WiN = i;
		}
		i++;
	}
	printf("winner of song is %d with score of %.2f\n", WiN, winner);
	return 0; 
}

int score(int numJudges){
	int i = 0, min, max, score, ave, sum = 0;
	scanf("%d", &score);
	min = score;
	max = score;
	sum += score;
	while(i<= numJudges){
		scanf("%d", &score);
		if(score>max){
			max = score;
		}
		if(score<min){
			min = score;
			i++;
		}
		
	}		
	
	sum += score;
	sum <= min;
	sum >= max;
	ave =(double) (sum)/numJudges;
	return ave;
}
			
