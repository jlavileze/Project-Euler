def isPalindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False
        
a = range(500,1000)
b = range(500,1000)

max_pal = 0

for i in a:
    for j in b:
        if isPalindrome(i*j) and i*j > max_pal:
            max_pal = i*j
            
print max_pal


