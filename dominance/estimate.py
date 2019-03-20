#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random
from dominance1 import dominance
from rank import rank
from dominanceMain import dominanceMain
from fun.funUser import *
from population_init import population


def estimate(population, functionObject):
    # 为函数对象赋值新的种群个体
    functionObject.population = population
    # print("functionObject.population",population)

    # 计算新种群目标函数数值，并建立矩阵 funScore
    funScore = np.vstack((functionObject.objFun_1(), functionObject.objFun_2()))
    np.set_printoptions(suppress=True)
    funScore = np.transpose(funScore)      # 二维数组是转置效果
    # print("funScore",funScore)

    # 输入函数数值矩阵，求得个体 分层和拥挤距离 字典
    r_dict = dominance(funScore)
    layerDict = rank(r_dict)

    #ls = np.append(layerDict[1],layerDict[2])
    # print(ls)

    print(funScore[layerDict[1]])
    #print(funScore)


if __name__ == "__main__":
    '''
    np.random.seed(0)
    random.seed(0)
    from function.funUserDefine import *
    population=np.random.rand(10, 3)
    functionObject=ZDT1(population)
    print(dominanceMain(population, functionObject))
    print(estimate(population,functionObject))
    '''

    p = population(10, 4)
    #print(p)
    f = MinMax(p)
    #print(dominanceMain(p,f))
    estimate(p,f)


