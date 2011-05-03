#include <stdio.h>

int factorCount(int m)
{
	int n, i, factors, found;

	n = m;
	i = 2;
	factors = 1;
	found = 0;
	while (n > 1) {
		if (n % i == 0) {
			if (factors % i != 0) {
				factors *= i;
				found += 1;
			}
			n /= i;
		} else {
			i++;
		}
	}

	return found;
}

int main(void)
{
	int i, consecutive, n, factors;

	i = 1;
	consecutive = 0;
	n = 4;
	while (1) {
		if (i % 1000 == 0) {
			printf("Progress: %d\n", i);
		}

		factors = factorCount(i);
		if (factors == n) {
			consecutive += 1;
			if (consecutive == n) {
				printf("%d\n", i - n + 1);
				break;
			}
		} else {
			consecutive = 0;
		}
		i++;
	}
}
