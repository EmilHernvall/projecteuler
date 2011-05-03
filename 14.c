#include <stdio.h>

#define func(n) (((n)&1)?(3*(n)+1):((n)/2))

int main(void)
{
	int i, maxStart = 0, maxCount = 0;
	for (i = 1; i < 1000000; i++) {
		int steps = 0;
		unsigned long long n = i;
		do {
			steps++;
		} while ((n = func(n)) != 1);

		if (steps > maxCount) {
			maxCount = steps;
			maxStart = i;
		}
	}

	printf("max: %d with %d steps\n", maxStart, maxCount);

	return 0;
}
