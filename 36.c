#include <stdio.h>

int reverseBinary(int n)
{
	int m = 0;
	while (n > 0) {
		m = (m << 1) | (n & 1);
		n = n >> 1;
	}

	return m;
}

int reverseDenary(int n)
{
	int m = 0;
	while (n > 0) {
		m = m * 10 + (n % 10);
		n = n / 10;
	}

	return m;
}

int main(void)
{
	int sum = 0;
	int i = 0;
	while (i < 1000000) {
		if (i == reverseDenary(i) && i == reverseBinary(i)) {
			printf("%d\n", i);
			sum += i;
		}
		i++;
	}
	printf("sum: %d\n", sum);
}
