#include <stdio.h>
#include <string.h>

void permute(char *str, char *buf, char before, int mask)
{
	int len = strlen(str);
	int i, j = 0;
	for (i = 0; i < len; i++) {
		if (mask & (1 << i)) {
			continue; 
		} else {
			j = 1;
			printf("%c", str[i]);
			permute(str, buf, str[i], mask | (1 << i));
		}
	}

	if (j == 0) {
		printf("\n");
	}
}

int main(void)
{
	char str[] = "abcd";
	char buf[sizeof(str)];
	int len = strlen(str);

	int permutations = 1;
	int i;
	for (i = 1; i <= len; i++) {
		permutations *= i;
	}

	printf("permutations: %d\n", permutations);
	permute(str, buf, 0, 0);

	return 0;
}
