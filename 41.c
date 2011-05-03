#include <stdio.h>
#include <string.h>

int c = 0;

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

	c++;

    return 1;
}

int permute(char *str, char *buf, int pos, int mask)
{
//	c++;

	int len = strlen(str);
	int i, j = 0, max = 0, v;
	for (i = 0; i < len; i++) {
		if (mask & (1 << i)) {
			continue; 
		} else {
			j = 1;
			buf[pos] = str[i];
			v = permute(str, buf, pos + 1, mask | (1 << i));
			if (v > max) {
				max = v;
			}
		}
	}

	if (j == 0) {
		int prime = atoi(buf);
		if (isPrime(prime)) {
			return prime;
		}
	} else {
		return max;
	}
}

int main(void)
{
	char str[11];
	char buf[sizeof(str)];

	memset(str, 0, 10);
	memset(buf, 0, 10);

	int i, max = 0, v;
	for (i = 1; i < 9; i++) {
		str[i-1] = i + '0';
		v = permute(str, buf, 0, 0);
		if (v > max) {
			max = v;
		}
	}

	printf("permuations: %d\n", c);
	printf("max: %d\n", max);

	return 0;
}
