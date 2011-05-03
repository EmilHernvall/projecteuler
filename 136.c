#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
	int find = 50000000;
	int *solutions = malloc(sizeof(int)*(find + 1));
	memset(solutions, 0, sizeof(solutions));

	int i, j, n, max = (int)sqrt(find)+1;
	double d;
	for (i = 1; i < max; i++) {
		printf("%d\n", i);
		for (j = i; j < find+1; j++) {
			n = i*j;
			if (n > find) {
				break;
			}
	
			d = (i+j)/4.0;
//			printf("%d %d %d %f\n", n, i, j, fabs(d - (int)d));

			if (fabs(d - (int)d) < 0.0001 && i - d > 0) {
//				printf("i-sol\n");
				solutions[n]++;
			}

			if (fabs(d - (int)d) < 0.0001 && j - d > 0 && i != j) {
//				printf("j-sol\n");
				solutions[n]++;
			}
		}
	}
	printf("\n");
	int count = 0;
	for (i = 0; i <= find; i++) {
		if (solutions[i] == 1) {
//			printf("%d: %d\n", i, solutions[i]);
			count++;
		}
	}
	printf("count: %d\n", count);

	return 0;

}

