#include <stdio.h>
#include <string.h>

inline int toInt(char i)
{
	return i - '0';
}

void permute(char *str, char *buf, int pos, int mask)
{
	int len = strlen(str);
	int i, j = 0;
	for (i = 0; i < len; i++) {
		if (mask & (1 << i)) {
			continue; 
		} else {
			j = 1;
			buf[pos] = str[i];
			permute(str, buf, pos + 1, mask | (1 << i));
		}
	}

	if (j == 0) {
		if (((100 * toInt(buf[1]) + 10 * toInt(buf[2]) + toInt(buf[3])) % 2 == 0) &&
			((100 * toInt(buf[2]) + 10 * toInt(buf[3]) + toInt(buf[4])) % 3 == 0) &&
			((100 * toInt(buf[3]) + 10 * toInt(buf[4]) + toInt(buf[5])) % 5 == 0) &&
			((100 * toInt(buf[4]) + 10 * toInt(buf[5]) + toInt(buf[6])) % 7 == 0) &&
			((100 * toInt(buf[5]) + 10 * toInt(buf[6]) + toInt(buf[7])) % 11 == 0) &&
			((100 * toInt(buf[6]) + 10 * toInt(buf[7]) + toInt(buf[8])) % 13 == 0) &&
			((100 * toInt(buf[7]) + 10 * toInt(buf[8]) + toInt(buf[9])) % 17 == 0)) {
	
			printf("%s+", buf);
		}
	} 
}

int main(void)
{
	char str[] = "0123456789";
	char buf[sizeof(str)];

	memset(buf, 0, sizeof(buf));
	permute(str, buf, 0, 0);
	printf("0\n");

	return 0;
}
