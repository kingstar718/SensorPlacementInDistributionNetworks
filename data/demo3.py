'''
for i in range(12):     # 数字为模拟次数
    i = i+1
    print("elif",(i-1)*809,"<=i[0]<=",i*809-1,":","a[n]=",(i-1)*10)   # 数字为节点个数
'''  


import pandas as pd
import numpy as np


l = pd.read_csv('f:/test8091.csv',header=None)

p = np.array(l)
#print(p)

for i in range(p.shape[0]):
    p[i][i] = 1

newl = pd.DataFrame(data=p)
newl.to_csv('f:/test8092.csv', encoding='utf8')