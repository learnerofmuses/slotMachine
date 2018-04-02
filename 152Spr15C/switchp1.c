/*test 1 modified*/

double aveLast(); 
int countSeven(int n);

int main(){
	int choice, n;
	double ave;
	printf("enter choice\n");
	scanf("%d", &choice);
	switch(choice){
		case 1:
			printf("enter int:\n");
			scanf("%d", &n);
			if(n>0){
				printf("%d sevens\n", countSeven(n));
			}
			else{
				printf("invalid input\n");
			}
			break;
		case 2:
			ave=aveLast();
			if(ave==-1){
				printf("empty input\n");
			}
			else{
				printf("%d\n", ave);
			{
			break;
		default:
			printf("invalid choice\n");
			break;
	}
	return 0;
}


double aveLast(){
	int count = 0, num, sum=0;
	double res;
	printf"enter positives\n");/*optional*/
	scanf("%d", &num);
	while(num>0){
		sum = sum+num%10;
		count++;
		scanf("%d", &num);
	}
	if(count>0){
		res=(double)(sum)/count;
	}
	else{
		res=-1;
	}
	return res;
}

int countSeven(int n){
	int c=0;
	while(n>0){
		if(n%10==7){
			c++;
		}
		n = n/10;
	}
	return c;
}


