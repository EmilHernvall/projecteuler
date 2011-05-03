#include <stdio.h>
#include <math.h>
#include <string.h>

#define max(a,b) ((a)>(b)?(a):(b))

void add(const char *t1, const char *t2, char **out)
{
	int len1 = strlen(t1);
	int len2 = strlen(t2);

	int bufLen = max(len1,len2)+1;
	char *buf = (char*)malloc((bufLen + 1) * sizeof(char));
	memset(buf, '0', bufLen*sizeof(char));

	char *p1 = t1 + len1 - 1, *p2 = t2 + len2 - 1, *p3 = buf + bufLen - 1;
	int extra = 0;
	while (1) {
		int n1 = 0, n2 = 0;

		if (p1 >= t1) {
			n1 = *p1 - '0';
			p1--;
		}

		if (p2 >= t2) {
			n2 = *p2 - '0';
			p2--;
		}

		int sum = n1 + n2 + extra;
		extra = sum >= 10 ? 1 : 0;
//		printf("%d %d %d %d\n", n1, n2, sum % 10, extra);

		*p3 = (sum % 10) + '0';
		p3--;

		if (p2 < t2 && p1 < t1) {
			break;
		}
	}

	*out = buf;
}

int main(void)
{
	char *res = "2";
	int i = 0;
	for (i = 1; i < 1000; i++) {
		add(res,
			res,
			&res);
	}

	printf("%s\n", res);
	int sum = 0;
	for (i = 0; i < strlen(res); i++) {
		sum += res[i] - '0';
	}

	printf("sum: %d\n", sum);

	return 0;
}
