#include <cs50.h>
#include <math.h>
#include <stdio.h>

int exponent_p(int n, int r, int p);

int main(void) {
    printf("%i\n", exponent_p(10,3,5));
}

int exponent_p(int n, int r, int p) {
    // p is a prime
    int total = 0;
    int j = 1;
    while(n/(pow(p,j)) > 0) {
        int summand = floor(n/pow(p,j)) - floor(r/pow(p,j)) - floor((n-r)/pow(p,j));
        total += summand;
        j++;
    }
    return total;
}