import numpy as np

p = np.array([1,2,5,6,4,3,4])
p1 = p.copy()
p2 = p
p[0]=3
print(p,p1,p2)