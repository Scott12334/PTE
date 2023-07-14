// C program to illustrate
// read system Call
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main()
{
	int fd, sz;
	char* c = (char*)calloc(100, sizeof(char));

	fd = open("password.txt", 0);
	if (fd < 0) {
		perror("r1");
		exit(1);
	}

	sz = read(fd, c, 64);
	printf("Those bytes are as follows: % s\n", c);

	return 0;
}

