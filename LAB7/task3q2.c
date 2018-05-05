#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<fcntl.h>
int main(){
char buff[256];
int n=0;

 int fd = open("newFile.txt",O_WRONLY|O_CREAT,0777);
 int fd2 = open("f1.txt",O_RDONLY|O_CREAT,0777);
	while(1)
        {

	 n=read(fd2,buff,256);
		if(n<=1)
                {
		  exit(-n);
		}
       
	write(fd,buff,n);
	 }

return 0;
}