#include <stdio.h>
#include <math.h>

int isPrime(int n)
{
    if (n == 2)
        return 1;
    if (n == 5)
        return 1;

    int end = n % 10;
    if (end != 1 && end != 3 && end != 7 && end != 9)
        return 0;

    int i = 3;
	int root = sqrt(n);
    while (i <= root) {
        if (n % i == 0)
            return 0;
        i = i + 2;
	}

    return 1;
}

int main(void)
{
	int i = 3;
	unsigned long long sum = 2;
	while (i <= 2000000)
	{
	    if (isPrime(i))
    	    sum += i;
		if (i % 1001 == 0)
			printf("%d\n", i);

		i = i + 2;
	}

	printf("\n");
	printf("sum: %lld\n", sum);
}
