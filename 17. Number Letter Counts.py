from num2words import num2words

total = 0

def count_letters(word):
    total = 0
    for char in word:
        if char.isalpha():
            total += 1
    return total

for i in range(1,1001):
    total += count_letters(str(num2words(i)))
    
print total
