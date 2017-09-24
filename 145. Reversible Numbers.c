#include <stdio.h> 
#include <cs50.h>
#include <string.h>
#include <math.h>

bool isOdd(int x);
int reverse(int x);
bool odd_digits(int x);
int sum_reverse(int x);

int main(void) {
    int counter = 0;
    for (int n = 10; n < 1000000000; n++) {
        int rev_candidate = sum_reverse(n);
        if (odd_digits(rev_candidate) && n%10 != 0) {
            counter += 1;
        }
    }
    printf("%i\n", counter);
}

bool odd_digits(int x) {
    while (x > 0) {
        if (!isOdd(x%10)) {
            return false;
        }
        x = x/10;
    }
    return true;
}

int sum_reverse(int x) {
    return x + reverse(x);
}

int reverse(int x) {
    int reverse = 0;
    while (x > 0) {
        reverse = reverse * 10 + (x % 10);
        x = x/10;
    }
    return reverse;
}

bool isOdd(int x) {
    if (x % 2 == 1) {
        return true;
    }
    else {
        return false;
    }
}