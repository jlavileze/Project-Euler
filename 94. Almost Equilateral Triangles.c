#include <cs50.h>
#include <math.h>
#include <stdio.h>

int case_two(int a);

int main(void) {
    // int upper_lim = 333333335;
    // long long sum_perimeters = 0;
    printf("%i\n",case_two(5));
}

// int case_one(int a) {
//     // pseudo_area = 8 * area
//     int pseudo_area = 3 * pow(a,3) - pow(a,2) - 3 * a + 1;
//     return pseudo_area;
// }

int case_two(int a) {
    // pseudo_area = 8 * area
    int pseudo_area = 3 * pow(a,3) + pow(a,2) - 3 * a - 1;
    return pseudo_area;
}