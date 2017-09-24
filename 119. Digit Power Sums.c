#include <stdio.h>
#include <math.h>
#include <cs50.h>


int sum_digits(int x);
double digit_power_sum(int x);
double logab(double number, double base);
bool isInt(double x);



int main(void){
    int counter = 0;
    for (long i = 11; i < 1000000000; i++) {
        float z = digit_power_sum(i);
        if (isInt(z)) {
            counter += 1;
            printf("a(%ld) = %f\n", i,z);
        }
        if (counter == 30) {
            printf("A_30 = %ld\n", i);
            break;
        }
    }
}

double digit_power_sum(int x) {
    int y = sum_digits(x);
    return logab(x,y);
}

double logab(double number, double base) {
    if (base == 1) {
        return 0.5;
    }
    else {
        return log(number)/log(base);        
    }
}


bool isInt(double x) {
    return x == floor(x);
}


int sum_digits(int x){
    int sum = 0;
    while (x != 0) {
        sum = sum + (x%10);
        x = x/10;
    }
    return sum;
}