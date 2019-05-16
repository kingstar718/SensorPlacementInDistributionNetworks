#!/usr/bin/env python
# encoding:UTF-8
from funModel import *
from itertools import chain
import pandas as pd
# 以下为具体实现函数
# 需要用户自定义函数，继承与上面的模板抽象函数
class MinMax(objectFun_2):

    def __init__(self, population, timematrix):
        objectFun_2.__init__(self, population)
        self.timematrix = timematrix

    def objFun_1(self):
        p = self.timematrix     # 时间矩阵
        p_list = []
        for x in self.population:   #population为种群  x为个体  i为一个节点索引
            p_result = 0
            for i in x:
                p_sum = 0
                for p_num in range(p.shape[0]):  # 迭代从0->p.shape[0]-1
                    # print(p[p_num][i])
                    p_i = p[p_num][i]  # 取出行号为p_num和列号为i的数值
                    p_sum = p_sum + p_i
                # print(p_sum)
                p_result = p_result + p_sum
            p_list.append(p_result)     # 返回个体总的监测时间  越小越好
        return p_list

    def objFun_2(self):
        p_timematrix = self.timematrix
        unmonitoredresult = []

        for x in self.population:
            monitorednode = []
            for i in x:
                for p_num in range(p_timematrix.shape[0]):  # 迭代从0->p.shape[0]-1
                    if p_timematrix[p_num][i] != 0:  # 假设 时间 !=0 为有效的监测事件
                        monitorednode.append(p_num)  # 将检测到的事件编号放入list

            monitorednode = list(set(monitorednode))    # 除去单个个体监测到的重复监测点
            monitored = (len(monitorednode) / (p_timematrix.shape[0]))  # 计算所有能监测到的事件与所有事件之比
            unmonitored = 1-monitored     #
            unmonitored = float('%.3f' % unmonitored)   # 乘以1000000使目标值相似
            unmonitoredresult.append(unmonitored)  # 将目标二的值放入list    # 返回未能监测到的事件比例  越小越好
        return unmonitoredresult

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


# 使用字典先行存储信息, 使用时直接拿出来
class MinMax2(objectFun_2):
    def __init__(self, population, nodeDirt):
        objectFun_2.__init__(self, population)
        self.nodeDirt = nodeDirt

    def objFun_1(self):
        pDirt = self.nodeDirt  # 时间字典
        p_list = []
        for x in self.population:  # population为种群  x为个体  i为一个节点索引
            p_result = []
            for i in x:
                p_result.append(pDirt[i][1])
            nodeTime = sum(p_result)/len(x)
            p_list.append(nodeTime)  # 返回个体平均的监测时间  越小越好
        return p_list

    def objFun_2(self):
        pDirt = self.nodeDirt  # 时间字典
        unmonitoredresult = []

        for x in self.population:
            monitorednode = []
            for i in x:
                monitorednode.append(pDirt[i][0])
            monitorednode = set(list(chain(*monitorednode)))
            monitored = len(monitorednode)/len(pDirt)
            unmonitored = 1 - monitored
            unmonitored = float('%.3f' % unmonitored)
            unmonitoredresult.append(unmonitored)
        return unmonitoredresult


# 设置每个节点带有权重的目标函数计算
class MinMax3(objectFun_2):

    def __init__(self, population, nodeDirt):
        objectFun_2.__init__(self, population)
        self.nodeDirt = nodeDirt

    # 时间计算
    def objFun_1(self):
        pDirt = self.nodeDirt  # 时间字典
        p_list = []
        for x in self.population:  # population为种群  x为个体  i为一个节点索引
            p_result = []
            for i in x:
                #nodeTime = pDirt[i][1]
                #CPnodeTime = nodeTime*float(pDirt[i][2])*10000      # 将概率添加进去
                #p_result.append(CPnodeTime)
                p_result.append(pDirt[str(i)][1])
            nodeTime = sum(p_result)/len(x)
            p_list.append(nodeTime)  # 返回个体平均的监测时间  越小越好
        return p_list

    # 覆盖率计算
    def objFun_2(self):
        pDirt = self.nodeDirt  # 时间字典
        unmonitoredresult = []

        for x in self.population:
            monitorednode = []
            for i in x:
                monitorednode.append(pDirt[str(i)][0])
            monitorednode = set(list(chain(*monitorednode)))
            monitored = 0
            # 3 以管长*管径来计算概率
            for i in monitorednode:
                monitored = monitored + float(pDirt[str(i)][3])
            '''
            # 2 单以管长来计算
            for i in monitorednode:
            monitored = monitored + float(pDirt[str(i)][2])
            '''
            # monitored = len(monitorednode)*(1/3628)       # 1.平均概率
            #monitored = len(monitorednode)/len(pDirt)
            unmonitored = 1 - monitored
            unmonitored = float('%.3f' % unmonitored)
            unmonitoredresult.append(unmonitored)
        return unmonitoredresult


# 测试函数  如下
if __name__ == "__main__":
    from timematrix.generatetimematrix import generate_timematrix
    import csv
    from population_init import population
    import numpy as np
    import pandas as pd
    #np.random.seed(0)
    #zdt1=ZDT1(np.random.rand(20, 3))    #　生成行２０列３的随机矩阵
    #print("objFun_1",zdt1.objFun_1())
    #print("objFun_2",zdt1.objFun_2())
    #p = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,13,14,15,16]])
    #print(p)
    #p=np.array([[1,2,3],[4,5,6]])
    '''
    exe1 = "F:/AWorkSpace/test/EPANETDEMO.exe"
    input1 = "F:/AWorkSpace/test/Net2.inp"
    rpt1 = "F:/AWorkSpace/test/Net2.rpt"
    sourcequality1 = 200000  # 投入的污染物mg数
    duration1 = 10800  # 水力模拟时间参数
    qual_reportstep1 = 600  # 水质步长与报告间隔时间
    qualindex1 = 4
    regularmatch1 = '  [0-9]'
    nodeCount1 = 36
    net2_matrix1 = generate_timematrix(exe1,input1,rpt1,sourcequality1,duration1,qual_reportstep1,qualindex1,regularmatch1,nodeCount1)
    net_pop = population(30, 5, 36)
    net2_value = MinMax(net_pop,net2_matrix1)
    print(net2_value.objFun_1())
    print(net2_value.objFun_2())
    '''
    '''
    exe2 = "F:/AWorkSpace/test/EPANETDEMO.exe"
    input2 = "F:/AWorkSpace/test/ky2.inp"
    rpt2 = "F:/AWorkSpace/test/ky2.rpt"
    sourcequality2 = 200000  # 投入的污染物mg数
    duration2 = 36000  # 水力模拟时间参数  36000
    qual_reportstep2 = 600  # 水质步长与报告间隔时间
    qualindex2 = 4
    regularmatch2 = '  J'
    nodeCount2 = 809
    ky2_matrix2 = generate_timematrix(exe2, input2, rpt2, sourcequality2, duration2, qual_reportstep2, qualindex2,
                                      regularmatch2, nodeCount2)

    print(ky2_matrix2)
    p = population(100,50,809)

    m = MinMax(p,ky2_matrix2)
    print(m.objFun_1())
    print(m.objFun_2())'''
    matrixpath = "D:\\Git\\SensorPlacementInDistributionNetworks\\timematrix\\max.csv"
    matrix = pd.read_csv(matrixpath, header=None)
    matrix = np.array(matrix)
    p = population(200, 80, 3628)
    import time
    start = time.time()
    #m = MinMax(p, matrix)

    #print(m.objFun_1())
    #print(m.objFun_2())
    #print("目标函数计算时间: ", time.time() - start)

    nodeDirt = computeMatrix(matrixpath).computeNodeDirt()
    sss = time.time()
    m2 = MinMax2(p, nodeDirt)
    print(m2.objFun_1())
    print(m2.objFun_2())
    print("目标函数计算时间: ", time.time()-sss)

    import json
    jsonFile = "F:\\AWorkSpace\\data\\3628node.json"
    with open(jsonFile, "r") as f:
        nodeJson = json.load(f)
    nodeDirt2 = json.loads(nodeJson)
    m3 = MinMax3(p, nodeDirt2)
    print(m3.objFun_1())
    print(m3.objFun_2())






