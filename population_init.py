import numpy as np
import random


# 通过节点总数确定list
def createList(nodeCount):
    l = []
    for i in range(nodeCount):
        i = int(i)
        l.append(i)
    return l

def population(p_num,i_num,nodeNum):
    # l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,30,31,3,32,33,34,5,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91]
    l = createList(nodeNum)
    population_list=[]
    for p in range(p_num):
        i_list=random.sample(l,i_num)   # 从list中拿不重复个数的list
        population_list.append(i_list)  # 根据种群规模加入到大的list中
    population_list = np.array(population_list)   # 将初始的list改为np的list
    #population_list=np.sort(population_list)    # 排序
    return population_list


if __name__ == "__main__":
    p = population(10,5,809)
    print(p)