#include <stdio.h> 
// #include <cs50.h>
#include <string.h>
#include <math.h>
// #include "numbertheory.h"

long phi(long n);
long sum_phi(long n);

int main(void) {
    double total = 0;
    long upper_lim = 500000000;
     
    for (long i = 1; i < upper_lim; i += 2) {
        total += sum_phi(i);
        if ((i-1) % 100000 == 0) {
            printf("i = %ld\n", i);
        }
    }
    
    printf("%f\n", total);
}

long sum_phi(long n) {
    // Sum of phi(n^i) mod(n+1) with 1<=i<=n
    if (n % 2 == 0) {
        return 0;
    }
    else {
        return phi(n);
    }
}

long phi(long n)
{    
    long result = n;   // Initialize result as n
 
    // Consider all prime factors of n and subtract their
    // multiples from result
    for (int p=2; p*p<=n; ++p)
    {
        // Check if p is a prime factor.
        if (n % p == 0)
        {
            // If yes, then update n and result 
            while (n % p == 0)
                n /= p;
            result -= result / p;
        }
    }
 
    // If n has a prime factor greater than sqrt(n)
    // (There can be at-most one such prime factor)
    if (n > 1)
        result -= result / n;
    return result;
}