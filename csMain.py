# !/usr/bin/env python
# encoding:UTF-8
import numpy as np
import random
import pandas as pd
from function.funUserDefine import *
from selection.selection import selection
from crossover import crossover
from mutation import mutation
from dominance.dominanceMain import dominanceMain
from dominance.estimate import estimate
from population_init import population

import matplotlib.pyplot as plt

def main(nodeCount,xN, yN, alfa, belta, iterationnum):

    # 初始化种群
    pop = population(xN, yN, nodeCount)
    matrix = pd.read_csv(matrixpath, header=None)
    timematrix = np.array(matrix)
    nodeDirt = computeMatrix(matrixpath).computeNodeDirt()
    #  计算目标函数
    functionObject = MinMax2(pop, nodeDirt)     # 第二种方式计算
    #functionObject = MinMax(pop, timematrix)

    for i in range(iterationnum):
        f_population = pop.copy()  # 浅拷贝
        selection(pop, functionObject)  # 选择
        crossover(pop, alfa)  # 交叉
        mutation(pop, belta, nodeCount-1)  # 变异
        c_population = pop
        temp_population = np.vstack((f_population, c_population))  # 合并两个数组
        #functionObject = MinMax(temp_population, timematrix)
        functionObject = MinMax2(temp_population, nodeDirt)
        pop = dominanceMain(temp_population, functionObject)  # 从合并种群中返回一半好的种群
        print("第", i, "次迭代")
        # print(population)
        '''
        n = len(np.array(list(set([tuple(t) for t in population]))))
        if n<20:
            break
        '''
    estimate(pop, functionObject)
    '''
    for i in population:
        print(i)
    '''
    pop_node = np.array(list(set([tuple(t) for t in pop])))
    for i in pop_node:
        print(i)

    funScore1 = np.vstack((functionObject.objFun_1(), functionObject.objFun_2()))
    np.set_printoptions(suppress=True)
    funScore = np.transpose(funScore1)

    a1 = funScore1[0]
    a2 = funScore1[1]
    plt.scatter(a1, a2)
    plt.xlabel("MinTime")
    plt.ylabel("Uncovered")
    plt.show()


if __name__ == '__main__':

    # 200个个体, 30个变量， 变量数值范围0到2**14
    # 交叉概率0.6， 编译概率0.1
    xN1 = 500
    yN1 = 100
    alfa1= 0.9
    belta1 = 0.2
    iterationnum1 = 3000
    nodeCount1 = 3628
    #matrixpath = "D:\\Git\\SensorPlacementInDistributionNetworks\\timematrix\\max.csv"
    matrixpath = "timematrix//max.csv"
    main(nodeCount1, xN1,yN1,alfa1, belta1, iterationnum1)
