#include <stdio.h>

int factorial(int f)
{
	if (f == 0) {
		return 1;
	}

	return (f == 1) ? 1 : (factorial(f-1) * f);
}

int main(void)
{
	int factorials[10];
	unsigned int i;
	for (i = 0; i < 10; i++) {
		factorials[i] = factorial(i);
	}

	unsigned int totalSum = 0, sum, j;
	for (i = 10; i < 8*factorials[9]; i++) {
		sum = 0;
		j = i;
		while (j > 0) {
			sum += factorials[j%10];
			j /= 10;
		}
		if (sum == i) {
			printf("%d\n", i);
			totalSum += i;
		}
	}
	printf("total sum: %d\n", totalSum);

	return 0;
}

