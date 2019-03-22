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
from population_init import population
from timematrix.generatetimematrix import generate_timematrix
import matplotlib.pyplot as plt

def main(exepath, inpath, rptpath, sourcequality, duration, qual_reportstep, qualindex, regularmatch, nodeCount,xN, yN, alfa, belta, iterationnum):

    # 初始化种群
    pop = population(xN, yN, nodeCount)
    timematrix = generate_timematrix(exepath, inpath, rptpath, sourcequality, duration, qual_reportstep, qualindex, regularmatch, nodeCount)
    #  计算目标函数
    functionObject = MinMax(pop, timematrix)

    for i in range(iterationnum):
        f_population = pop.copy()  # 浅拷贝
        selection(pop, functionObject)  # 选择
        crossover(pop, alfa)  # 交叉
        mutation(pop, belta, nodeCount-1)  # 变异
        c_population = pop
        temp_population = np.vstack((f_population, c_population))  # 合并两个数组
        functionObject = MinMax(pop, timematrix)
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
    '''
    # 200个个体, 30个变量， 变量数值范围0到2**14
    # 交叉概率0.6， 编译概率0.1
    xN1 = 200
    yN1 = 8
    alfa1= 0.9
    belta1 = 0.2
    iterationnum1 = 1000

    exe1 = "F:/AWorkSpace/test/EPANETDEMO.exe"
    input1 = "F:/AWorkSpace/test/Net2.inp"
    rpt1 = "F:/AWorkSpace/test/Net2.rpt"
    sourcequality1 = 200000  # 投入的污染物mg数
    duration1 = 36000  # 水力模拟时间参数
    qual_reportstep1 = 600  # 水质步长与报告间隔时间
    qualindex1 = 4
    regularmatch1 = '  [0-9]'
    nodeCount1 = 36
    main(exe1, input1, rpt1,sourcequality1, duration1, qual_reportstep1, qualindex1, regularmatch1, nodeCount1,xN1, yN1, alfa1, belta1, iterationnum1)

    '''
    xN2 = 300
    yN2 = 30
    alfa2= 0.9
    belta2 = 0.2
    iterationnum2 = 100
    # random.seed(0)
    # np.random.seed(0)
    exe2 = "F:/AWorkSpace/test/EPANETDEMO.exe"
    input2 = "F:/AWorkSpace/test/ky2.inp"
    rpt2 = "F:/AWorkSpace/test/ky2.rpt"
    sourcequality2 = 200000  # 投入的污染物mg数
    duration2 = 36000  # 水力模拟时间参数  36000
    qual_reportstep2 = 600  # 水质步长与报告间隔时间
    qualindex2 = 4
    regularmatch2 = '  J'
    nodeCount2 = 809

    main(exe2,input2, rpt2, sourcequality2, duration2, qual_reportstep2, qualindex2, regularmatch2, nodeCount2, xN2, yN2, alfa2, belta2, iterationnum2)
