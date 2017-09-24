f = open("p022_names.txt", 'r')

list_as_str = sorted(f.read().replace('"','').split(','),key=str)

test_str = 'PEPE","RADU","ASAD","ED'


#test_output = test_str.split('\",\"')
#print test_output

#list_of_names = list_as_str.split('\",\"')

#list_of_names.sort()

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

def list_alphabetic_score(lonames):
    total_score = 0
    for item in lonames:
        total_score = total_score + int(name_score(item)) * int(lonames.index(item))
    return total_score

test_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]

print list_alphabetic_score(list_as_str)


# For some weird reason Python is returning a KeyError '\xe2'. The code runs for any other list, but there seems
# to be a problem with the imported list.

## Answer = 871198282
    
    
    
    
    
    
    
    