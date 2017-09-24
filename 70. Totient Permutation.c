#include <stdio.h> 
#include <cs50.h>
#include <string.h>
#include <math.h>

// Declaration of non-main functions


float n_over_phi(float n);
// int totient(int n);
// bool isPermutation(string a, string b);
// bool isContained(char a, string b);
// bool isTotientPerm(int a);
int phi(int n);
bool hasSameDigits (long num1, long num2);

// Array of primes



//  Main: Project Euler Problem 70: Totient Permutations


// int main(void) {
//     int x = totient(87109);
//     printf("%i\n", x);
// }

// int main(void) {
//     int x = phi(5592449);
//     int y = isTotientPerm(x);
    
//     printf("%i\n", x);
//     printf("%i\n", y);
// }

int main(void) {
    int min_n = 0;
    float min_ratio = 100;
    
    int upper_bound = 10000000;
    for (int i = 100; i < upper_bound; i++) {
        
        int phi_i = phi(i);
        
        if (hasSameDigits(i, phi_i)) {
            // printf("phi(%i) = %i\n", i, phi(i));
            float n_ratio = n_over_phi(i);
            if (n_ratio < min_ratio) {
                min_ratio = n_ratio;
                min_n = i;
            }
        }
    }
    printf("Minimal totient permutation at n = %i\n", min_n);
}


// bool isTotientPerm(int a) {
//     char a_str[64];
//     char b_str[64];
//     int y = phi(a);
    
    
//     sprintf(a_str, "%i" , a);
//     sprintf(b_str, "%i", y);
    
//     return isPermutation(a_str,b_str);
// }

////////// Totient functions //////////////////


float n_over_phi(float n) {
    return n/phi(n);
}



// int totient(int n) {
//     double inner = 1;
//     float upper = n/2 + 1;
//     int k = n;
//     for (int i = 0; i < len_primes; i++) {
//         if (primes[i] > upper) {
//             break;
//         }
//         else if (k % primes[i] == 0) {
//             inner = inner * (1-1.0/primes[i]);
//             k = k / primes[i];
//         }
//     }
//     return n * inner;
// }


//////////// Permutation helper functions ////////////////////


// bool isPermutation(string a, string b) {
//     int a_len = strlen(a);
//     int b_len = strlen(b);
    
//     bool result = true;
    
//     if (a_len != b_len) {
//         return false;
//     } //exit if
//     else {
//         for (int j = 0; j < a_len; j++) {
//             char jth_char = a[j];
//             result = result && isContained(jth_char,b);
//         }
//         return result;
//     }
// }

// bool isContained(char a, string b) {
//     bool result = false;
//     int str_len = strlen(b);
    
//     for (int i = 0; i < str_len; i++) {
//         if (b[i] == a) {
//             result = true;
//             break;
//         }
//     }
//     return result;
// }

int phi(int n)
{    
    int result = n;   // Initialize result as n
 
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

bool hasSameDigits (long num1, long num2) {
    int digits[10];
    int i;

    for (i = 0; i < 10; i++)      // Init all counts to zero.
        digits[i] = 0;

    while (num1 != 0) {           // Process all digits.
        digits[num1%10]++;        // Increment for least significant digit.
        num1 /= 10;               // Get next digit in sequence.
    }

    while (num2 != 0) {           // Same for num2 except decrement.
        digits[num2%10]--;
        num2 /= 10;
    }

    for (i = 0; i < 10; i++)
        if (digits[i] != 0)       // Any count different, not a permutation.
            return false;

    return true;                  // All count identical, was a permutation.
}