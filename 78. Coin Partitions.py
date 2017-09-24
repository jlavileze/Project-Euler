partition_array = [0 for i in range(1000000)]

partition_array[0] = 1
partition_array[1] = 1
partition_array[2] = 2
partition_array[3] = 3
partition_array[4] = 5
partition_array[5] = 7
partition_array[6] = 11
partition_array[7] = 15
partition_array[8] = 22
partition_array[9] = 30
partition_array[10] = 42
partition_array[11] = 56
partition_array[12] = 77
partition_array[13] = 101
partition_array[14] = 135
partition_array[15] = 176
partition_array[16] = 231
partition_array[17] = 297
partition_array[18] = 385
partition_array[19] = 490
partition_array[20] = 627
partition_array[21] = 792
partition_array[22] = 1002
partition_array[23] = 1255
partition_array[24] = 1575
partition_array[25] = 1958
partition_array[26] = 2436
partition_array[27] = 3010
partition_array[28] = 3718
partition_array[29] = 4565

def partitions(n):
    total = 0
    if n < 0:
        return 0
    
    elif partition_array[n] != 0:
        return partition_array[n]
   
    else:
        for k in range(1,n):
            first_term = int(n - (0.5 * k * ((3 * k) - 1)))
            second_term = int(n - (0.5 * k * ((3 * k) + 1)))
            leading = int((-1) ** (k+1))
            
            
            total += (leading * (partitions(first_term) + partitions(second_term)))
    
    return total


for i in range(55300,100000):
    if i % 100 == 0:
        print i

    ith_partition = partitions(i)
    
    if ith_partition % 1000000 == 0:
        print "P(" + str(i) + ") = " + ith_partition
        break
    
    partition_array[i] = ith_partition
    
    

