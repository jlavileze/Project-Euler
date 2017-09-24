from math import sqrt

max_test = 1389026624
min_test = 1010101010

for i in range(min_test,max_test,10):
    i_squared = i ** 2
    if (i_squared/100) % 10 == 9:
        if (i_squared/10000) % 10 == 8:
            if (i_squared/1000000) % 10 == 7:
                if (i_squared/100000000) % 10 == 6:
                    if (i_squared/10000000000) % 10 == 5:
                        if (i_squared/1000000000000) % 10 == 4:
                            if (i_squared/100000000000000) % 10 == 3:
                                if (i_squared/10000000000000000) % 10 == 2:
                                    if (i_squared/1000000000000000000) % 10 == 1:
                                        print i_squared

print sqrt(1929374254627488900)