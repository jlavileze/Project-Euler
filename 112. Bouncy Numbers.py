def isIncreasing(x):
    x_str = str(x)
    list_num = [int(c) for c in x_str]
    
    return all(x<=y for x, y in zip(list_num, list_num[1:]))
    
def isDecreasing(x):
    x_str = str(x)
    list_num = [int(c) for c in x_str]
    
    return all(x>=y for x, y in zip(list_num, list_num[1:]))
    
counter = 0
for i in range(1,21780000):
    if not isIncreasing(i):
        if not isDecreasing(i):
            counter += 1
            ratio = float(counter) / i
            if ratio >= 0.99:
                print i
                break
    


