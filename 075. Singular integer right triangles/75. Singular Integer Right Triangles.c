#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>


int right_perimeter(int m, int n, int k);
int gcd (int a, int b);


int main(void) {
    
    int length = 1500001;
    int perimeters[length];
    
    for (int i = 0; i < length; i++) {
        perimeters[i] = 0;
    }
    
    for (int m = 2; m < 5000; m++) {
        for (int n = 1; n < m; n++) {
            // for(int k = 1; k < 200000; k++) {
                if ((m+n) % 2 == 1 && gcd(m,n) == 1) {
                    for(int k = 1; k < 125000; k++) {
                        int perimeter = right_perimeter(m,n,k);
                        if (perimeter > 1500000) {
                            break;
                        }
                        perimeters[perimeter]++;
                    }
                    
                }
                
                
                // if (perimeter > 1500000) {
                //     break;
                // }
                
                // perimeters[perimeter]++;
                
                // while(perimeter <= 1500000) {
                //     perimeter += perimeter;
                //     if (perimeter > length) {
                //         break;
                //     }
                //     perimeters[perimeter]++;
                // }
                
            // }
        }
    }
    
    int total = 0;
    
    for (int j = 0; j < length; j++) {
        if (perimeters[j] == 1) {
            total++;
        }
    }
    printf("%i\n", total);
}



int right_perimeter(int m, int n, int k) {
    return 2 * k * m * (m + n);
    // int a = k * (m*m - n*n);
    // int b = 2*k*m*n;
    // int c = k * (m*m + n*n);
    // return a+b+c;
}

int gcd (int a, int b)
{
  int c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}