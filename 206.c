#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int match(unsigned long long in)
{
	unsigned long long n = in;
	int i;
	for (i = 0; i < 19; i++) {
		if (i % 2 == 0) {
			if ((n % 10) != ((10 - i / 2) % 10)) {
				return 0;
			}
		}
		n /= 10;
	}
	return 1;
}

int main(void)
{
	unsigned long long base = 1020304050607080900;
	unsigned long long min = 1020304050607080900;
	unsigned long long max = 1929394959697989990;
	unsigned long long minRoot = sqrt(min);
	unsigned long long maxRoot = sqrt(max);

	unsigned long long i;
	for (i = minRoot; i < maxRoot; i += 10) {
		unsigned long long n = i*i;
		if (i % 10000000 == 0) {
			printf("%lld of %lld\n", i, maxRoot);
		}
		if (match(n)) {
			printf("solution: %lld\n", i);
			break;
		}
	}

	return 0;
}
