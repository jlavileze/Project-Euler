def isPerm(x,y):
    x_str = str(x)
    y_str = str(y)
    if sorted(x_str) == sorted(y_str):
        return True
    else:
        return False


for i in range(100000,1000000):
    if isPerm(i,i*2) and isPerm(i,i*3) and isPerm(i,i*4) and isPerm(i,i*5) and isPerm(i,i*6):
        print i