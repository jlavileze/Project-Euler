import numpy as np
from math import acos, pi

origin = (0,0)

def vector_angle(v1,v2):
    ### v1 and v2 are two-dimensional numpy arrays
    cos_theta = np.inner(v1,v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return acos(cos_theta)

def isContained(a,b,c):
    ### a,b,c are 2-ples representing triangle coordinates in R2
    v1 = np.array(a[0],a[1])
    v2 = np.array(b[0],b[1])
    v3 = np.array(c[0],c[1])
    
    theta1 = vector_angle(v1,v2)
    theta2 = vector_angle(v2,v3)
    theta3 = vector_angle(v3,v1)
    
    sum_angles = theta1 + theta2 + theta3
    print sum_angles
    error = abs(2.0 * pi - sum_angles)
    
    if error < 0.000001:
        return True
    else:
        return False

isContained(np.array([-175,41]),np.array([-421,-714]),np.array([574,-645]))

print 2* pi
