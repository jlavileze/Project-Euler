from math import sqrt, log
import decimal

decimal.getcontext().prec = 5

def nth_fibonacci(n):
    f = decimal.Decimal(((1 + sqrt(5)) ** n - (1- sqrt(5)) ** n) / ((2 ** n) * sqrt(5)))
    return f
    
#i = 1
#while True:
 #   if log(nth_fibonacci(i), 10) >= 1000:
  #      print i
   #     break
    #else:
     #   i += 1

## Need to solve overflow error