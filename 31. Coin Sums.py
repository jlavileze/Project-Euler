[1,2,5,10,20,50,100,200]

counter = 0

for a in range(2):
    for b in range(3):
        for c in range(5):
            for d in range(11):
                for e in range(21):
                    for f in range(41):
                        for g in range(101):
                            for h in range(201):
                                value = h + 2*g + 5*f + 10*e + 20*d + 50*c + 100*b + 200*a
                                if value > 200:
                                    break
                                elif value == 200:
                                    counter += 1
                                        
                                        

print counter