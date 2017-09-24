def collatz_seq(seed):
    col_seq = [seed]
    while seed > 1:
        if seed % 2 == 0:
            seed = seed/2
        else:
            seed = 3*seed+1
        col_seq.append(seed)
    return col_seq
    
def max_len_seq_upto(x):
    max_len = 0
    max_len_seed = 1
    for i in range(1,x):
        len_col = len(collatz_seq(i))
        if len_col > max_len:
            max_len = len_col
            max_len_seed = i
    return max_len_seed

print max_len_seq_upto(1000000)