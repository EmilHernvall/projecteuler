#include <stdio.h>
#include <string.h>

int c = 0;

void permute(char *str, char *buf, int pos, int mask)
{
	int len = strlen(str);
	int i, j = 0;
	for (i = 0; i < len; i++) {
		if (mask & (1 << i)) {
			continue; 
		} else {
			j = 1;
			buf[pos] = str[i];
			permute(str, buf, pos + 1, mask | (1 << i));
		}
	}

	if (j == 0) {
		c++;

		if (c == 1000000) {
			printf("%s\n", buf);
			exit(0);
		}
	}
}

int main(void)
{
	char str[] = "0123456789";
	char buf[sizeof(str)];
	int len = strlen(str);
	buf[len] = 0;

	int permutations = 1;
	int i;
	for (i = 1; i <= len; i++) {
		permutations *= i;
	}

	printf("permutations: %d\n", permutations);
	permute(str, buf, 0, 0);

	return 0;
}
