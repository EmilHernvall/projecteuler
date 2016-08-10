#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <limits.h>

#define min(a,b) \
  ({ __typeof__ (a) _a = (a); \
      __typeof__ (b) _b = (b); \
    _a < _b ? _a : _b; })

#define max(a,b) \
  ({ __typeof__ (a) _a = (a); \
      __typeof__ (b) _b = (b); \
    _a > _b ? _a : _b; })

#define BOUND 0x1000000000000000

uint64_t y(uint64_t n, uint64_t k, uint64_t x0, uint64_t x1) {
    uint64_t x;
    if (k == 0) {
        x = 0;
    } else if (k == 1) {
        x = 1;
    } else if (k % 2 == 0) {
        x = (2*x0 + 3*x1) % BOUND;
    } else {
        x = (3*x0 + 2*x1) % BOUND;
    }

    if (k >= n) {
        return x;
    } else {
        return BOUND - max(y(n, 2*k, x1, x),
                           y(n, 2*k+1, x1, x));
    }
}

int64_t y2(int64_t n,
           int64_t k,
           int64_t x0,
           int64_t x1,
           int64_t alpha,
           int64_t beta,
           uint8_t max) {
    uint64_t x;
    if (k == 0) {
        x = 0;
    } else if (k == 1) {
        x = 1;
    } else if (k % 2 == 0) {
        x = (2*x0 + 3*x1) % BOUND;
    } else {
        x = (3*x0 + 2*x1) % BOUND;
    }

    if (k >= n) {
        return x;
    } else {
        if (max) {
            int64_t v = LLONG_MIN;

            v = max(v, y2(n, 2*k, x1, x, alpha, beta, 0));
            alpha = max(alpha, v);

            if (beta <= alpha) {
                return v;
            }

            v = max(v, y2(n, 2*k+1, x1, x, alpha, beta, 0));
            return BOUND - v;
        } else {
            int64_t v = LLONG_MAX;

            v = min(v, y2(n, 2*k, x1, x, alpha, beta, 1));
            beta = min(beta, v);

            if (beta <= alpha) {
                return v;
            }

            v = min(v, y2(n, 2*k+1, x1, x, alpha, beta, 1));
            return BOUND - v;
        }
    }
}

uint64_t A(uint64_t n) {
    return y(n, 1, 0, 0);
}

int64_t A2(int64_t n) {
    return y2(n, 1, 0, 0, LLONG_MIN, LLONG_MAX, 1);
}

int main(int argc, char* argv[]) {

    uint64_t n = atoll(argv[1]);
    printf("%ld\n", A(n));
    printf("%ld\n", A2(n));

    return 0;
}
