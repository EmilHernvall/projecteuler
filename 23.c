#include <stdio.h>
#include <math.h>

int main(void)
{
	int nrs[28123];
	int i, j, n, max, sum, sum2 = 0;

	memset(nrs, 0, sizeof(nrs));

	j = 1;
	while (j <= 28123) {
		i = 2;
		n = j;
		sum = 1;
		max = n;
		while (i < max) {
			if (n % i == 0) {
				max = n / i;
				if (i != max) {
					sum += i + max;
				} else {
					sum += i;
				}
			}
			i++;
		}

		if (sum > j) {
			// abundant
			//printf("abundant: %d: %d\n", j, sum);
			nrs[j] = 1;
		} else {
			// deficient
		}

		int k, m = 0;
		for (k = 1; k < j; k++) {
			//printf("\tj: %d, k: %d, nrs[k]: %d, nrs[j-k]: %d\n", j, k, nrs[k], nrs[j-k]);
			if (nrs[k] == 1 && nrs[j-k] == 1) {
				m = 1;
				break;
			}
		}

		if (!m) {
			sum2 += j;
			printf("%d: %d\n", j, sum);
		} else {
		}

		j++;
	}

	printf("sum: %d\n", sum2);
}
