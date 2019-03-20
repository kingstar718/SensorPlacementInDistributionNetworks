import csv
import numpy as np
from population_init import population


def fitness_pop(pop):
    def perfect_pareto_front():  # 将csv中的数据拿出来,构成一个[[0 0 0.5] [0 0 0.5] [0.458 0.154 0.2545]...]这样的矩阵
        with open('D:/Git/nsga2_python-master/SensorPlacementInDistributionNetworks/timematrix.csv', encoding='utf8') as file:
            p = [list(map(float, row)) for row in csv.reader(file)]
            return np.array(p)

    def fitness(x):
        result = []
        p = perfect_pareto_front()

        p_result = 0
        for i in x:
            p_sum = 0
            for p_num in range(p.shape[0]):  # 31 迭代0-30
                # print(p[p_num][i])
                p_i = p[p_num][i]  # 取出行号为p_num和列号为i的数值
                p_sum = p_sum + p_i
            # print(p_sum)
            p_result = p_result + p_sum
        # p_result = 0 - p_result
        # print(p_result)
        result.append(p_result)  # 将目标一的值放入list

        l = []
        for i in x:
            for p_num in range(p.shape[0]):
                if (p[p_num][i] < 50):  # 假设时间超过50分钟的设定为无效的监测事件
                    # print("shixiao")
                    l.append(p_num)  # 将未检测到的事件编号放入list
                    l = list(set(l))
                    # print(l)
        l = list(set(l))
        m = (len(l) / (p.shape[0]))  # 计算所有未能监测到的事件与所有事件之比
        m = float('%.3f' % m)
        # print(m)
        m = (1-m) # 未被覆盖的事件的百分比
        result.append(m)  # 将目标二的值放入list
        return result
    l=[]

    for i in range(pop.shape[0]):
        m = fitness(pop[i])
        l.append(m)
    #print(l)
    np.set_printoptions(suppress=True)      # 不使用科学计数
    l=np.array(l,dtype=float)
    return l


def fitness(x):
    result = []
    p=perfect_pareto_front()

    p_result=0
    for i in x:
        p_sum = 0
        for p_num in range(p.shape[0]): #31 迭代0-30
            #print(p[p_num][i])
            p_i = p[p_num][i]   # 取出行号为p_num和列号为i的数值
            p_sum = p_sum+p_i
        #print(p_sum)
        p_result = p_result + p_sum
    #print(p_result)

    result.append(p_result)     # 将目标一的值放入list

    l=[]
    for i in x:
        for p_num in range(p.shape[0]):
            if(p[p_num][i]<50):     # 假设时间超过50分钟的设定为无效的监测事件
                #print("shixiao")
                l.append(p_num)     # 将未检测到的事件编号放入list
                l=list(set(l))
                #print(l)
    l = list(set(l))
    m = (len(l)/(p.shape[0]))   # 计算所有未能监测到的事件与所有事件之比
    m = float('%.3f' % m)
    #print(m)
    result.append(m)       # 将目标二的值放入list
    return result


def perfect_pareto_front():     # 将csv中的数据拿出来,构成一个[[0 0 0.5] [0 0 0.5] [0.458 0.154 0.2545]...]这样的矩阵
    with open('./timematrix.csv', encoding='utf8') as file:
        p = [list(map(float, row)) for row in csv.reader(file)]
        return np.array(p)


if __name__ == "__main__":
    p = population(4,3)
    print(p)
    print(fitness_pop(p))
