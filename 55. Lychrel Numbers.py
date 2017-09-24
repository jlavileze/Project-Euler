def isPalindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False
        

def isLychrel(x):
    for i in range(51):
        x_rev = int(str(x)[::-1])
        sum_of_revs = x + x_rev
        if isPalindrome(sum_of_revs):
            return False
        else:
            x = sum_of_revs
    else:
        return True

total = 0

for i in range(10000):
    if isLychrel(i):
        total += 1
        
print total