#!/usr/bin/env python
# encoding:UTF-8
from function.funModel import *
from itertools import chain


# 以下为具体实现函数
# 需要用户自定义函数，继承与上面的模板抽象函数
# 使用字典先行存储信息, 使用时直接拿出来
class MinMax2(objectFun_2):
    def __init__(self, population, node_dirt):
        objectFun_2.__init__(self, population)
        self.node_dirt = node_dirt

    def objFun_1(self):
        pDirt = self.node_dirt  # 时间字典
        p_list = []
        for x in self.population:  # population为种群  x为个体  i为一个节点索引
            p_result = []
            for i in x:
                p_result.append(pDirt[str(i)][1])
            node_time = sum(p_result)/len(x)
            p_list.append(node_time)  # 返回个体平均的监测时间  越小越好
        return p_list

    def objFun_2(self):
        node_dirt = self.node_dirt  # 时间字典
        unmonitored_result = []
        # 监测的总事件数
        sum_thing = []
        for i in node_dirt.values():
            sum_thing.append(i[0])
        sum_thing = set(list(chain(*sum_thing)))

        for x in self.population:
            monitored_node = []
            for i in x:
                monitored_node.append(node_dirt[str(i)][0])
            monitored_node = set(list(chain(*monitored_node)))
            monitored = len(monitored_node) / len(sum_thing)
            unmonitored = 1 - monitored
            unmonitored = float('%.3f' % unmonitored)
            unmonitored_result.append(unmonitored)
        return unmonitored_result


# 设置每个节点带有权重的目标函数计算
class MinMax3(objectFun_2):
    def __init__(self, population, node_dirt):
        objectFun_2.__init__(self, population)
        self.node_dirt = node_dirt

    # 时间计算
    def objFun_1(self):
        node_dirt = self.node_dirt  # 时间字典
        p_list = []
        for x in self.population:  # population为种群  x为个体  i为一个节点索引
            p_result = []
            for i in x:
                #nodeTime = pDirt[i][1]
                #CPnodeTime = nodeTime*float(pDirt[i][2])*10000      # 将概率添加进去
                #p_result.append(CPnodeTime)
                p_result.append(node_dirt[str(i)][1])
            nodeTime = sum(p_result)/len(x)
            p_list.append(nodeTime)  # 返回个体平均的监测时间  越小越好
        return p_list

    # 覆盖率计算
    def objFun_2(self):
        node_dirt = self.node_dirt  # 时间字典
        unmonitored_result = []
        for x in self.population:
            monitored_node = []
            for i in x:
                monitored_node.append(node_dirt[str(i)][0])
            monitored_node = set(list(chain(*monitored_node)))
            '''
            # 3 以管长*管径来计算概率
            for i in monitorednode:
                monitored = monitored + float(pDirt[str(i)][3])
            # 2 单以管长来计算
            for i in monitorednode:
            monitored = monitored + float(pDirt[str(i)][2])
            '''
            monitored=0
            for i in monitored_node:
                monitored = monitored + float(node_dirt[str(i)][4])
            #monitored = len(monitorednode)*(1/66383)       # 1.平均概率

            #monitored = len(monitorednode)/len(pDirt)
            unmonitored = 1 - monitored
            unmonitored = float('%.3f' % unmonitored)
            unmonitored_result.append(unmonitored)
        return unmonitored_result


# 测试函数  如下
if __name__ == "__main__":
    from population_init import population
    import numpy as np
    import json
    jsonFile = "F:\\AWorkSpace\\data\\3628node.json"
    with open(jsonFile, "r") as f:
        nodeJson = json.load(f)
    nodeDirt2 = json.loads(nodeJson)
    p = population(500,100, 3628)
    m3 = MinMax2(p, nodeDirt2)
    print(m3.objFun_1())
    print(m3.objFun_2())






