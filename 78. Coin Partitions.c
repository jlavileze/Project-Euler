#include <stdio.h> 
#include <cs50.h>
#include <string.h>
#include <math.h>

long modular_partitions(int n);
long partition_array[111000];

int main(void) {
    partition_array[0] = 1;
    partition_array[1] = 1;
    partition_array[2] = 2;
    partition_array[3] = 3;
    partition_array[4] = 5;
    partition_array[5] = 7;
    partition_array[6] = 11;
    partition_array[7] = 15;
    partition_array[8] = 22;
    partition_array[9] = 30;
    partition_array[10] = 42;
    partition_array[11] = 56;
    partition_array[12] = 77;
    partition_array[13] = 101;
    partition_array[14] = 135;
    partition_array[15] = 176;
    partition_array[16] = 231;
    partition_array[17] = 297;
    partition_array[18] = 385;
    partition_array[19] = 490;
    partition_array[20] = 627;
    partition_array[21] = 792;
    partition_array[22] = 1002;
    partition_array[23] = 1255;
    partition_array[24] = 1575;
    partition_array[25] = 1958;
    partition_array[26] = 2436;
    partition_array[27] = 3010;
    partition_array[28] = 3718;
    partition_array[29] = 4565;
    
    for (int k = 30; k < 111000; k++) {
        if (k % 100 == 0) {
            printf("%i\n", k);
        }
        
        long kth_partition = modular_partitions(k);
        
        if (kth_partition % 1000000 == 0) {
            printf("P(%i) = %ld\n", k, kth_partition);
            break;
        }
        
        partition_array[k] = kth_partition;
    }
}

long modular_partitions(int n) {
    // The partitions function includes the number itself as a possible partition
    // To count all partitions composed of at least two integers, then subtract 1 from the answer.
    long sum = 0;
    
    if (n < 0) {
        return 0;
    }
    
    else if(partition_array[n] != 0) {
        return partition_array[n];
    }
    
    else {
        for (int k = 1; k < n; k++) {
            long first_term_arg = n - (0.5 * k * ((3 * k) - 1));
            long second_term_arg = n - (0.5 * k * ((3 * k) + 1));
            
            if (k % 2 == 0) {
                sum -= (modular_partitions(first_term_arg) + modular_partitions(second_term_arg)) % 1000000;
            }
            
            else {
                sum += (modular_partitions(first_term_arg) + modular_partitions(second_term_arg)) % 1000000;
            }
           
        }
    }
    
    return sum % 1000000;
}