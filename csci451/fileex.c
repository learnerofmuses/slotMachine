#include <stdio.h>
#include <fntl.h>

int main(){
	if(argc < 2){
		printf("Error: must provide filename.\n");
		return 0; 
	int fid = open(argv[1], 0_RDWR);
	if(fid < 0){
		printf("Error: file %s not found.\n", argv[1]);
		return 0; 
	}
	char buffer[10];
	read(fid, buffer, 7); 
	buffer[7] = '\0';
	printf("%s\n", buffer);
	lseek(fid, -5, SEEK_END);
	write(fid, "how", 3);
	return 0; 
}
