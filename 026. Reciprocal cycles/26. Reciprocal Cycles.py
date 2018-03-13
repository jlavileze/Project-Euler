# import sys
# sys.setrecursionlimit(2000)
def repeating_long_division(num,den,digits,lorem):
    if num % den == 0:
        return digits
    elif den > 10 * num:
        digits += "0"
        return repeating_long_division(10*num, den, digits,lorem)
    elif den > num:
        return repeating_long_division(10*num, den, digits,lorem)
    else:
        quot = num // den
        rem = num % den
        
        if rem in lorem:
            return digits
        else:
            digits += str(quot)
            lorem.append(rem)
            return repeating_long_division(rem, den, digits, lorem)

def count_rec_str(d):
    return len(repeating_long_division(1,d,"",[]))

longest = 0
max_d = 1

for i in range(1,1000):
    if count_rec_str(i) > longest:
        longest = count_rec_str(i)
        max_d = i

print max_d, longest

