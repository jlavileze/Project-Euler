L = []

L.append("75")
L.append("95 64")
L.append("17 47 82")
L.append("18 35 87 10")
L.append("20 04 82 47 65")
L.append("19 01 23 75 03 34")
L.append("88 02 77 73 07 63 67")
L.append("99 65 04 28 06 16 70 92")
L.append("41 41 26 56 83 40 80 70 33")
L.append("41 48 72 33 47 32 37 16 94 29")
L.append("53 71 44 65 25 43 91 52 97 51 14")
L.append("70 11 33 28 77 73 17 78 39 68 17 57")
L.append("91 71 52 38 17 14 91 43 58 50 27 29 48")
L.append("63 66 04 68 89 53 67 30 73 16 69 87 40 31")
L.append("04 62 98 27 23 09 70 98 73 93 38 53 60 04 23")

M = []

M = [i.split() for i in L]
M = [[int(j) for j in i] for i in M]

print len(M)


## The greedy algorithm below is a bit buggy. However, notice that the solution is not
## given by this algorithm

def greedy_algorithm(lolists):
    total = 0
    counter = 0
    list_length = len(lolists)
    index_x = 0
    index_y = 0
    while counter < list_length-1:
        total += lolists[index_x][index_y]
        index_x += 1
        counter += 1
        if lolists[index_x][index_y] < lolists[index_x][index_y+1]:
            index_y += 1
    return total
    
print greedy_algorithm(M)
    