from math import sqrt

def side_length(a,b):
    delta_x = b[0] - a[0]
    delta_y = b[1] - a[1]
    ab = sqrt(delta_x ** 2 + delta_y ** 2)
    return ab

def area_triangle(a,b,c):
    x = side_length(a,b)
    y = side_length(b,c)
    z = side_length(c,a)
    s = 0.5 * (x+y+z)
    
    area = sqrt(s*(s-x)*(s-y)*(s-z))
    
    return area

def area_to_origin(a,b,c):
    t1 = area_triangle(a,b,(0,0))
    t2 = area_triangle(a,c,(0,0))
    t3 = area_triangle(b,c,(0,0))
    return t1+t2+t3

with open('p102_triangles.txt', 'rb') as triangles_txt:
    triangles = triangles_txt.readlines()

triangles2 = [i.strip('\n') for i in triangles]

triangles3 = [i.split(',') for i in triangles2]

counter = 0

for c in triangles3:
    x = (int(c[0]),int(c[1]))
    y = (int(c[2]),int(c[3]))
    z = (int(c[4]),int(c[5]))
    a1 = area_triangle(x,y,z)
    a2 = area_to_origin(x,y,z)
    if abs(a1-a2) < 1:
        counter += 1

print counter