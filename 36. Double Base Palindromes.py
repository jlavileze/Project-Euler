def dec_to_bin(x):
    remainders = []
    while x>0:
        remainders.append(x % 2)
        x = x/2
    reverse_remainders = remainders[::-1]
    bin_str = ""
    for i in reverse_remainders:
        bin_str = bin_str + str(i)
    return bin_str
    

def isPalindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False
        

sum_of_palindromes = 0

for i in range(10**6):
    if isPalindrome(i):
        i_bin = dec_to_bin(i)
        if isPalindrome(i_bin):
            sum_of_palindromes += i
            
print sum_of_palindromes
