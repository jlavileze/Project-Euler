triangles = []
squares = []
pentagons = []
hexagons = []
heptagons = []
octagons = []

# Generate triangular numbers
for n in range(200):
    t = int(n*(n+1)*0.5)
    if t > 9999:
        break
    elif t >= 1000:
        triangles.append(t)

# Generate square numbers
for n in range(200):
    s = int(n**2)
    if s > 9999:
        break
    elif s >= 1000:
        squares.append(s)

# Generate pentagonal numbers

for n in range(200):
    p = int(n*(3*n-1)/2)
    if p > 9999:
        break
    elif p >= 1000:
        pentagons.append(p)

# Generate hexaonal numbers

for n in range(200):
    h = int(n*(2*n-1))
    if h > 9999:
        break
    elif h >= 1000:
        hexagons.append(h)

# Generate heptagonal numbers

for n in range(200):
    hp = int(n*(5*n-3)/2)
    if hp > 9999:
        break
    elif hp >= 1000:
        heptagons.append(hp)

# Generate octagonal numbers
for n in range(200):
    o = int(n*(3*n-2))
    if o > 9999:
        break
    elif o >= 1000:
        octagons.append(o)

def split_num(num):
    num_str = str(num)
    front = num_str[0:2]
    back = num_str[2:4]
    return (front, back)

split_num(1234)

list(map(split_num, octagons))

def front_back_intersect(list1, list2):
    parsed_list2 = [i[0] for i in list2]
    output = []
    for j in list1:
        if j[1] in parsed_list2:
            output.append(j)
    
    return output

triangle_tuple = list(map(split_num,triangles))
square_tuple = list(map(split_num,squares))

print front_back_intersect(triangle_tuple,square_tuple)
