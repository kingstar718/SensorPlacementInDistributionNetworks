import matplotlib.pyplot as plt
import numpy as np
'''
l = np.array([[1,2,3],[3,4,5]])
print(l[0])
plt.scatter(l[0],l[1])
plt.show()
'''
layDirt = {1:[2,3,4,1,1,4],2:[2,3,4,1,1,4],3:[2,3,4,1,1,4],4:[2,3,4,1,1,4],5:[2,3,4,1,1,4]}
for i in range(len(layDirt)):
    print(layDirt[i+1])
