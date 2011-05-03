#include <stdio.h>
#include <math.h>

int main(void)
{
	int t, i, j, n, max, maxCount, factorCount;

	j = 0;
	t = 0;
	maxCount = 0;
	while (1) {
		t += j;

		i = 2;
		n = t;
		factorCount = 0;
		max = n;
		while (i <= max) {
			if (n % i == 0) {
				max = n / i;
				factorCount += 2;
			}
			i++;
		}

		if (n > 0 && (int)pow((int)sqrt(n),2) == n) {
			factorCount++;
		}

		if (factorCount > maxCount) {
			maxCount = factorCount;
			printf("%d: %d: %d\n", j, t, factorCount);
		}

		if (factorCount >= 500) {
			printf("Found: %d\n", t);
			break;
		}

		j++;
	}
}
