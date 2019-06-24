#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random
from population_init import population

from dominance1 import dominance
from rank import rank
"""
拥挤距离计算
输入：
funScore=np.array([[1,2], [2,3], [2,2], [3,2], [4,3], [2,1], [3,1], [3,2], [3,3], [3,4]])

layerDict
{1: [4, 9], 2: [8], 3: [1, 3, 7], 4: [2, 6], 5: [0, 5]}
indicate 第五层 个体索引 [0, 5]
"""

# crowddist(funScore, layerDict[3])  输入为一个矩阵和一个list
def crowddist(funScore, indicate):
    # 求出该层　评分子矩阵
    indicate = np.array(indicate)     # 生成矩阵[1 3 7]
    score =funScore[indicate]       # 选择funScore的第 1 3 7 列

    # 求出集合中 不同属性的 范围
    # rangeVector=np.array([1.0, 1.0])
    maxVector = np.max(funScore, axis=0)      # 求funScore的最大值
    minVector = np.min(funScore, axis=0)
    rangeVector = (maxVector-minVector)*1.0   # 求范围   rangeVector是一个目标值[...  ...]数组
    # print("rangeVector",rangeVector)
    # if rangeVector == 0:
        # rangeVector = rangeVector+1    # 防止后面作为除数

    # 生成个体编号
    N=score.shape[0]    # 第一维的长度    N=3
    V=score.shape[1]    # # 第二维的长度  V=2
    indicateVector = np.arange(N)     # 生成从0开始到N的[] [0 1 2]
    indicateVectorT = indicateVector.reshape(N, 1)  # 改变数组形状 [[0] [1] [2]]

    # 生成 函数值和个体序号 矩阵
    dist=np.array([0.0]*N*V).reshape(N, V)      # [[ 0.  0.] [ 0.  0.] [ 0.  0.]]
    scoreIndicateMatrix = np.hstack((score, indicateVectorT))  # [[2 3 0]  [3 2 1]  [3 2 2]]

    scoreList = scoreIndicateMatrix.tolist()  # [[2, 3, 0], [3, 2, 1], [3, 2, 2]]

    for i in range(V):
        scoreList.sort(key=lambda x:x[i])
        
        i_a=scoreList[0][-1]    # 取第一行最后一位
        i_b=scoreList[-1][-1]   # 取最后一行最后一位
        #dist[i_a][i]=1000000000000000
        #dist[i_b][i]=1000000000000000
        i_a=int(i_a)    # 后添加的
        i_b=int(i_b)    # 后添加的
        dist[i_a][i]=100000000000000000000000
        dist[i_b][i]=100000000000000000000000

        for j in range(1, N-1):
            c=scoreList[j-1][i]
            d=scoreList[j+1][i]
            i_e=scoreList[j][-1]
            i_e=int(i_e)    # 后添加的
            dist[i_e][i] = d-c

    distVector = np.sum(dist/rangeVector, axis=1)    # 后加了双斜线
    #print(distVector,indicate)
    dist_indicate = indicate[np.argsort(distVector)].tolist()
    #print(dist_indicate)

    return dist_indicate[::-1]


if __name__ == "__main__":
    funScore=np.array([[1,2], [2,3], [2,2],[2,2],[2,2],[2,2],[2,2],[2,2],[2,2],[2,2], [3,2], [4,3], [2,1], [3,1], [3,2], [3,3], [3,4]])
    layerDict={1: [4, 9], 2: [8], 3: [1, 3, 7], 4: [2, 6], 5: [0, 5]}
    d= dominance(funScore)
    print(d)
    r = rank(d)
    print(r)
    #print(crowddist(funScore, layerDict[3]))
    print(crowddist(funScore, r[2]))

'''
    p = population(100, 4)
    #print(p)
    f = fitness_pop(p)
    #print(f)
    d = dominance(f)
    print("支配关系字典d:",d)
    r = rank(d)
    print("分层字典r:",r)
    c = crowddist(f,r[5])
    print(c)
'''

