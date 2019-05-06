from population_init import population
import time
from function.funUserDefine import *
from selection.selection import selection
from crossover import crossover
from mutation import mutation
from dominance.dominanceMain import dominanceMain
from dominance.estimate import estimate
from population_init import population
import numpy as np
import random
import pandas as pd

def computePopTime(p_num,i_num,nodeNum):
    '''
    计算生成种群的时间
    :param p_num:
    :param i_num:
    :param nodeNum:
    :return:
    '''
    start  =time.time()
    population(p_num, i_num, nodeNum)
    print(time.time()-start)


def computeNgsaTime(pop, matrixpath):
    # 初始化种群
    start = time.time()
    matrix = pd.read_csv(matrixpath, header=None)
    t2 = time.time()
    print("读取csv时间 " , t2-start)
    timematrix = np.array(matrix)
    t3 = time.time()
    print(" 排序时间 : ", t3-t2)
    #  计算目标函数
    functionObject = MinMax(pop, timematrix)
    print(functionObject.objFun_1())
    print(functionObject.objFun_2())
    print("计算目标函数时间: ", time.time()-t3)


def computeDirt(matrixpath):
    matrix = pd.read_csv(matrixpath, header=None)
    timematrix = np.array(matrix)
    print(timematrix)
    print(timematrix[:,1])      #选取节点的一列

class computeMatrix():
    def __init__(self, matrixpath):
        self.matrixpath = matrixpath
        self.matrix = pd.read_csv(self.matrixpath, header=None)
        self.timematrix = np.array(self.matrix)

    def computeNodeDirt(self):
        nodeDirt = {}
        for i in range(self.timematrix.shape[1]):
            #print(self.timematrix[:, i])
            nodeName = []
            nodeTime = []
            twoList = []
            for n,m in enumerate(self.timematrix[:, i]):
                # print(n,m)
                if m!=0:
                    nodeName.append(n)
                    nodeTime.append(m)
            #print("节点%d"%i , nodeName, nodeTime)
            if len(nodeTime)==0:
                timeSum = 0
            else:
                timeSum = sum(nodeTime) / len(nodeTime)
            twoList.append(nodeName)
            twoList.append(timeSum)
            nodeDirt[i] = twoList
            #print(i, twoList)
        print(nodeDirt)
        return nodeDirt


if __name__=="__main__":
    #computePopTime(500, 120, 3625) # 0.08776545524597168
    p = population(100, 50, 3625)
    pass
    # 200个个体, 30个变量， 变量数值范围0到2**14
    # 交叉概率0.6， 编译概率0.1
    xN1 = 100
    yN1 = 50
    alfa1 = 0.9
    belta1 = 0.2
    iterationnum1 = 30
    nodeCount1 = 3628
    matrixpath = "D:\\Git\\SensorPlacementInDistributionNetworks\\timematrix\\max.csv"
    #computeNgsaTime(p, matrixpath)
    #computeDirt(matrixpath)
    #m = computeMatrix(matrixpath).computeNodeDirt()
    #print(m[1][1])
    reMatrix = "..//timematrix//max.csv"
    m = computeMatrix(reMatrix).computeNodeDirt()
    print(m[1][1])