#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
from funModel import *
import csv
from population_init import population
### 以下为具体实现函数
### 需要用户自定义函数，继承与上面的模板抽象函数
#######################################################
class ZDT1(objectFun_2):
    # ZDT1函数
    def gFun(self):
        N=self.population.shape[1]-1
        return 1+np.sum(self.population[:,1:], axis=1)*9.0/N

    def objFun_1(self):
        return self.population[:,0]

    def objFun_2(self):
        temp=1-np.sqrt(self.population[:,0]/self.gFun())
        return self.gFun()*temp


class MinMax(objectFun_2):

    def objFun_1(self):
        def perfect_pareto_front(self):  # 将csv中的数据拿出来,构成一个[[0 0 0.5] [0 0 0.5] [0.458 0.154 0.2545]...]这样的矩阵
            with open('D:/Git/nsga2_python-master/SensorPlacementInDistributionNetworks/test2.csv', encoding='utf8') as file:
                p = [list(map(float, row)) for row in csv.reader(file)]
                return np.array(p)
        p = perfect_pareto_front(self)
        p_list = []
        for x in self.population:
            p_result = 0
            for i in x:
                p_sum = 0
                for p_num in range(p.shape[0]):  # 31 迭代0-30
                    # print(p[p_num][i])
                    p_i = p[p_num][i]  # 取出行号为p_num和列号为i的数值
                    p_sum = p_sum + p_i
                # print(p_sum)
                p_result = p_result + p_sum
            p_list.append(p_result)     # 返回个体总的监测时间  越小越好
        return p_list

    def objFun_2(self):
        def perfect_pareto_front(self):  # 将csv中的数据拿出来,构成一个[[0 0 0.5] [0 0 0.5] [0.458 0.154 0.2545]...]这样的矩阵
            with open('D:/Git/nsga2_python-master/SensorPlacementInDistributionNetworks/test2.csv', encoding='utf8') as file:
                p = [list(map(float, row)) for row in csv.reader(file)]
                return np.array(p)
        p = perfect_pareto_front(self)
        result = []
        for x in self.population:
            l = []

            for i in x:
                for p_num in range(p.shape[0]):
                    if (p[p_num][i] < 710):  # 假设时间超过50分钟的设定为无效的监测事件
                        #print(p[p_num][i])
                        # print("shixiao")
                        l.append(p_num)  # 将未检测到的事件编号放入list
                        l = list(set(l))
                        # print(l)
            l = list(set(l))
            m = (len(l) / (p.shape[0]))  # 计算所有未能监测到的事件与所有事件之比
            m = 1-m
            m = float('%.3f' % m)
            result.append(m)  # 将目标二的值放入list    # 返回未能监测到的事件比例  越小越好
            m = 0
        return result


#######################################################


# 测试函数  如下
if __name__=="__main__":
    #np.random.seed(0)
    #zdt1=ZDT1(np.random.rand(20, 3))    #　生成行２０列３的随机矩阵
    #print("objFun_1",zdt1.objFun_1())
    #print("objFun_2",zdt1.objFun_2())
    #p = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,13,14,15,16]])
    #print(p)
    #p=np.array([[1,2,3],[4,5,6]])
    p = population(100,4)
    print(p)
    m = MinMax(p)
    print(m.objFun_1())
    print(m.objFun_2())





