#!/usr/bin/env python
# encoding:UTF-8
import numpy as np
import random
from population_init import population
import copy

def crossover(population,alfa):
    old_population = copy.copy(population)
    N = population.shape[0]   # 行
    V = population.shape[1]   # 列

    for i in range(N-1):
        r = random.random()
        if r<alfa:
            i_p=V//2
            for n in range(i_p,V):      # 选择是在个体一半处进行交叉,交换两个个体的后半段
                mid=population[i][n]
                population[i][n]=population[i+1][n]
                population[i+1][n]=mid
    #for i in range(N-1):
        #population[i]=np.sort(population[i])    # 个体基因大小的排序
    for i in range(N):
        m = len(set(population[i]))
        if m<V:
            population[i] = old_population[i]


# 以下是测试用例
if __name__ == "__main__":
    np.random.seed(0)
    xN=5
    yN=3
    alfa=0.8
    p=population(5,6,13)

    print(p)
    crossover(p,alfa)
    print(p)






