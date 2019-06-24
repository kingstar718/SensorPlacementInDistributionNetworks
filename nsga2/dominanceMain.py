#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random
from dominance1 import dominance
from rank import rank
from crowddist import crowddist
from population_init import population


# 根据种群和相应的目标函数返回新的种群 # 因为之前合并了种群  所以返回了一半的种群
def dominanceMain(population, functionObject):
    # 为函数对象赋值新的种群个体
    functionObject.population = population

    # 计算新种群目标函数数值，并建立矩阵 funScore
    funScore=np.vstack((functionObject.objFun_1(), functionObject.objFun_2()))

    np.set_printoptions(suppress=True)  # 不使用科学计数

    funScore=np.transpose(funScore)   # 转置
    #print("funScore",funScore)

    N = population.shape[0]   # 获得矩阵的行数
    nN = N//2     # 更改为双斜线
    #nN = N
    # 输入函数数值矩阵，求得个体 分层和拥挤距离 字典
    r_dict=dominance(funScore)  # 关系字典{个体号码：[支配其的个数， 被其支配的个体列表]}
    # print(r_dict)
    layerDict=rank(r_dict)  # 分层字典layerDict {1:[3,1,4], 2:[2,0]}

    s = 0
    indicate = []

    for i in range(1, len(layerDict)+1):
        s += len(layerDict[i])
        if s < nN:
            indicate.extend(layerDict[i])
            continue
        elif s == nN:
            indicate.extend(layerDict[i])
            break
        else:
            s -= len(layerDict[i])
            temp=crowddist(funScore, layerDict[i])
            indicate.extend(temp[:nN-s])
            break

    for i in range(len(layerDict)):     # i从零开始 需要+1
        #print(layerDict[i+1])
        ceng_population = np.array(population[layerDict[i+1]])
        N = ceng_population.shape[0]
        n = len(np.array(list(set([tuple(t) for t in ceng_population]))))
        print("第 ", i, "层的重复率:", n/N, "--该层个体数量:", N, "--不重复个体数量:", n)

    print(len(indicate))
    # 返回新种群
    return population[indicate]


if __name__ == "__main__":
    #np.random.seed(0)
    #random.seed(0)     # 显示此行会固定初始化的种群
    #from function.funUserDefine import *
    #population=np.random.rand(10, 3)
    #print(population)
    #functionObject=ZDT1(population)
    #print(functionObject)
    #print(dominanceMain(population, functionObject))

    print("#################################")

    p = population(20, 3)
    #print(p)
    from fun.funUser import *
    f = MinMax(p)
    #print(f.objFun_1())
    #print(f.objFun_2())
    #d = dominanceMain(p, f)
    d = dominanceMain(p, f)
    print(d)

