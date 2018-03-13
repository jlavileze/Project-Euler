#include <math.h>
#include <stdio.h>

// #define LIMIT = 1000

void sieve(int n, int primes[]);
void squarefree_sieve(int n, int squarefree[]);
int is_hilbert(int x);

int main(void) {
    int i, n = 1000000000; // find the primes up to n
    int v[n];
    squarefree_sieve(n, v);
    int counter = 0;
    for (i = 0;i < n;i++)
        if (v[i] == 1 && is_hilbert(i))
            counter++;
    printf("%i\n", counter);
}

int is_hilbert(int x) {
    if ((x-1) % 4 == 0) {
        return 1;
    }
    else {
        return 0;
    }
}

void squarefree_sieve(int n, int squarefree[]) {
    
    for(int i = 0; i < n; i++) {
        squarefree[i] = 1;
    }
    
    int sqrt_n = floor(sqrt(n)) + 1;
    int primes[sqrt_n];
    sieve(sqrt_n, primes);
    
    for (int j = 0; j < sqrt_n; j++) {
        if(primes[j] == 1) {
            squarefree[j*j] = 0;
        }
    }
    
    int k,l;
    
    for (k=1; k < n; k++) {
        if(squarefree[k] == 0) {
            for (l = 2; l*k < n; l++) {
                squarefree[l*k] = 0;
            }
        }
    }
    
}

void sieve(int n, int primes[])
{
    int i, j;
    
    for (i = 0;i < n; i++)
        primes[i] = 1; // we initialize the sieve list to all 1's (True)
    
    primes[0] = 0;
    primes[1] = 0; // Set the first two numbers (0 and 1) to 0 (False)
    
    for (i = 2;i < sqrt(n); i++) // loop through all the numbers up to the sqrt(n)
        for (j = i*i;j < n; j+=i) // mark off each factor of i by setting it to 0 (False)
            primes[j] = 0;
}