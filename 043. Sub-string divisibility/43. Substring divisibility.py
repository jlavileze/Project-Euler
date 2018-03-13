# 0-9 pandigital number:
#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

#d2d3d4=406 is divisible by 2
#d3d4d5=063 is divisible by 3
#d4d5d6=635 is divisible by 5
#d5d6d7=357 is divisible by 7
#d6d7d8=572 is divisible by 11
#d7d8d9=728 is divisible by 13
#d8d9d10=289 is divisible by 17

# Implications:
# d4 = [0,2,4,6,8]
# (d3 + d4 + d5) % 3 == 0
# d6 = [0,5]
# (d6 - d7 + d8) % 11 == 0

from itertools import permutations

perms = [''.join(p) for p in permutations('0123456789')]
candidates = []

for perm in perms:
    if int(perm[1:4]) % 2 == 0:
        if int(perm[2:5]) % 3 == 0:
            if int(perm[3:6]) % 5 == 0:
                if int(perm[4:7]) % 7 == 0:
                    if int(perm[5:8]) % 11 == 0:
                        if int(perm[6:9]) % 13 == 0:
                            if int(perm[7:10]) % 17 == 0:
                                candidates.append(int(perm))



print candidates
print sum(candidates)