#include <stdio.h>
#include <stdlib.h>

static const int n = 21;

int main(void)
{
	unsigned long long grid[n][n];
	int i, j;

	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			if (i == 0 || j == 0) {
				grid[i][j] = 1;
			} else {
				grid[i][j] = 0;

				if (i > 0) {
					grid[i][j] += grid[i-1][j];
				}
				if (j > 0) {
					grid[i][j] += grid[i][j-1];
				}
			}

//			printf("%10lld ", grid[i][j]);
		}
//		printf("\n");
	}

	printf("%lld\n", grid[n-1][n-1]);

	return 0;
}
