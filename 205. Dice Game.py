peter = []

pyramid = [1,2,3,4]

for a in pyramid:
    for b in pyramid:
        for c in pyramid:
            for d in pyramid:
                for e in pyramid:
                    for f in pyramid:
                        for g in pyramid:
                            for h in pyramid:
                                for i in pyramid:
                                    event = a+b+c+d+e+f+g+h+i
                                    peter.append(event)

sample_space_peter = [i for i in range(9,37)]
universe_peter = len(peter)
distribution_peter = {}

def count_instances(x,lonums):
    counter = 0
    for item in lonums:
        if item == x:
            counter += 1
    return counter

for event in sample_space_peter:
    distribution_peter[event] = float(count_instances(event, peter))/universe_peter

colin = []

cube = [1,2,3,4,5,6]

for a in cube:
    for b in cube:
        for c in cube:
            for d in cube:
                for e in cube:
                    for f in cube:
                        event = a+b+c+d+e+f
                        colin.append(event)

sample_space_colin = [i for i in range(6,37)]
universe_colin = len(colin)
distribution_colin = {}

for event in sample_space_colin:
    distribution_colin[event] = float(count_instances(event,colin))/universe_colin

probability = 0

for p_key in distribution_peter:
    for c_key in distribution_colin:
        if p_key > c_key:
            probability += (distribution_peter[p_key]*distribution_colin[c_key])

print probability
