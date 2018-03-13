from math import sqrt
import re
import string

#generate a key to map the letters in our strings to
letters = string.ascii_uppercase
letters_map = {letter: idx for idx, letter in enumerate(string.ascii_uppercase, start=1)}

#open the file and parse on quoted values  
with open('p042_words.txt') as f:
    words = sorted(re.findall(r'"(.*?)"', f.read()))

print words

def isInt(x):
    if x - round(x) == 0:
        return True
    else:
        return False

def isTriangular(y):
    x = sqrt(2*y + 0.25) -0.5
    return isInt(x)
    

alphabetical_values = {"A": 1,
"B": 2,
"C": 3,
"D": 4,
"E": 5,
"F": 6,
"G": 7,
"H": 8,
"I": 9,
"J": 10,
"K": 11,
"L": 12,
"M": 13,
"N": 14,
"O": 15,
"P": 16,
"Q": 17,
"R": 18,
"S": 19,
"T": 20,
"U": 21,
"V": 22,
"W": 23,
"X": 24,
"Y": 25,
"Z": 26}

def name_score(name):
    score = 0
    for char in name:
        score = score + alphabetical_values[str(char)]
     
    return score  
    
    
counter = 0

for i in words:
    if isTriangular(name_score(i)):
        counter += 1
        
print counter
