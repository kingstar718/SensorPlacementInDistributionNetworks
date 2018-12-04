# coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename = "result.csv"
filename2 = "result2.csv"
filename3 = "result3.csv"
filename4 = "result4.csv"
filename5 = "3node50gen.csv"
df = pd.read_csv(filename5,header=None,sep=",",names=["最短监测时间","未被覆盖的比例"])
#print(df)
#fig = plt.figure()
#np.set_printoptions(suppress=True)
#list = np.array(df)
#print(list)
x = df["最短监测时间"]
y = df["未被覆盖的比例"]
plt.scatter(x,y)
plt.title("Pareto")
plt.xlabel("MinTime")
plt.ylabel("Uncovered")
plt.show()

