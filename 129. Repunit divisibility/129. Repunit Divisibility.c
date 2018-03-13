#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

int repunit_k(int k);
// int gcd (int a, int b);

int main(void) {
    for (int n = 2; n < 100; n++) {
        int last_dig = n%10;
        if (last_dig == 1 || last_dig == 3 || last_dig == 7 last_dig == 9) {
            for(int k = 1; k < 11; k++) {
                int rep = repunit_k(k);
            }
        }
    }
}

int repunit_k(int k) {
    int output = 1;
    while(k > 1) {
        output = output*10 + 1;
        k -= 1;
    }
    return output;
}

// int gcd (int a, int b)
// {
//   int c;
//   while ( a != 0 ) {
//      c = a; a = b%a;  b = c;
//   }
//   return b;
// }