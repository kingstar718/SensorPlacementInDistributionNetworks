# !/usr/bin/env python
# encoding:UTF-8
import numpy as np
import random
from function.funUserDefine import *
from selection.selection import selection
from crossover import crossover
from mutation import mutation
from dominance.dominanceMain import dominanceMain
from dominance.estimate import estimate

# 200个个体, 30个变量， 变量数值范围0到2**14
# 交叉概率0.6， 编译概率0.1
xN=500
yN=30
alfa=0.9
belta=0.2

# random.seed(0)
# np.random.seed(0)

# 测试population
population = population(200, 40, 809)
functionObject = MinMax(population)

for i in range(200):
    f_population = population.copy()   # 浅拷贝
    selection(population, functionObject)   # 选择
    crossover(population, alfa)     # 交叉
    mutation(population,  belta, 35)       # 变异
    c_population = population
    temp_population = np.vstack((f_population, c_population))     # 合并两个数组
    functionObject = MinMax(population)
    population = dominanceMain(temp_population, functionObject)   # 从合并种群中返回一半好的种群
    print("第", i, "次迭代")
    #print(population)
    '''
    n = len(np.array(list(set([tuple(t) for t in population]))))
    if n<20:
        break
    '''
estimate(population, functionObject)
'''
for i in population:
    print(i)
'''
pop_node = np.array(list(set([tuple(t) for t in population])))
for i in pop_node:
    print(i)

import matplotlib.pyplot as plt
funScore1 = np.vstack((functionObject.objFun_1(), functionObject.objFun_2()))
np.set_printoptions(suppress=True)
funScore = np.transpose(funScore1)

a1 = funScore1[0]
a2 = funScore1[1]
plt.scatter(a1, a2)
plt.xlabel("MinTime")
plt.ylabel("Uncovered")
plt.show()
