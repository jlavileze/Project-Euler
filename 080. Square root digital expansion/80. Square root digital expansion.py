from decimal import *




total = 0


for x in range(2,100):
    if x not in [4,9,16,25,36,49,64,81,100]:
        getcontext().prec = 101
        y = str(Decimal(x).sqrt()).replace(".","")
        print y[1:]
        for char in y[1:]:
            total += int(char)

print total

len('899494936611665341611821069467886549987703127638636512236758165935127349234749271952712740293491009')