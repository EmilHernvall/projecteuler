#include <stdio.h>
#include <stdlib.h>

#define MAX 1000000

int main(void)
{
	int pos, n, i;
	unsigned int *sieve = (unsigned int*)malloc(sizeof(unsigned int)*MAX);

	for (i = 0; i < MAX; i++) {
		sieve[i] = i;
	}

	pos = 2;
	n = 0;
	i = 0;
	while (pos < MAX) {
		while (pos < MAX && sieve[pos] == 0) {
			pos += 1;
		}

		if (pos == MAX) {
			break;
		}

		n = sieve[pos];
		sieve[pos] = 0;
		printf("%d\n", n);

		i = pos;
		while (i < MAX) {
			if (i % n == 0) {
				sieve[i] = 0;
			}
			i += n;
		}
	}
}
