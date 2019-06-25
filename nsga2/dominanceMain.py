#!/usr/bin/env python
#encoding:UTF-8
from numpy import vstack, set_printoptions, transpose, array
from dominance1 import dominance
from rank import rank
from crowddist import crowddist
from population_init import population


# 根据种群和相应的目标函数返回新的种群 # 因为之前合并了种群  所以返回了一半的种群
def dominanceMain(population, func_object):
    # 为函数对象赋值新的种群个体
    func_object.population = population

    # 计算新种群目标函数数值，并建立矩阵 funScore
    func_score = vstack((func_object.objFun_1(), func_object.objFun_2()))

    set_printoptions(suppress=True)  # 不使用科学计数

    func_score = transpose(func_score)   # 转置

    N = population.shape[0]   # 获得矩阵的行数
    nN = N//2     # 更改为双斜线
    #nN = N
    # 输入函数数值矩阵，求得个体 分层和拥挤距离 字典
    r_dict = dominance(func_score)  # 关系字典{个体号码：[支配其的个数， 被其支配的个体列表]}
    # print(r_dict)
    layer_dict = rank(r_dict)  # 分层字典layerDict {1:[3,1,4], 2:[2,0]}

    s = 0
    indicate = []

    for i in range(1, len(layer_dict)+1):
        s += len(layer_dict[i])
        if s < nN:
            indicate.extend(layer_dict[i])
            continue
        elif s == nN:
            indicate.extend(layer_dict[i])
            break
        else:
            s -= len(layer_dict[i])
            temp = crowddist(func_score, layer_dict[i])
            indicate.extend(temp[:nN-s])
            break

    for i in range(len(layer_dict)):     # i从零开始 需要+1
        #print(layerDict[i+1])
        ceng_population = array(population[layer_dict[i+1]])
        N = ceng_population.shape[0]
        n = len(array(list(set([tuple(t) for t in ceng_population]))))
        print("第 ", i, "层的重复率:", n/N, "--该层个体数量:", N, "--不重复个体数量:", n)

    print(len(indicate))
    # 返回新种群
    return population[indicate]


if __name__ == "__main__":
    #np.random.seed(0)
    #random.seed(0)     # 显示此行会固定初始化的种群
    #from function.funUserDefine import *
    #population=np.random.rand(10, 3)
    #print(population)
    #functionObject=ZDT1(population)
    #print(functionObject)
    #print(dominanceMain(population, functionObject))

    print("#################################")

    p = population(20, 3, 94)
    #print(p)
    from function.funUserDefine import *
    f = MinMax2(p)
    #print(f.objFun_1())
    #print(f.objFun_2())
    #d = dominanceMain(p, f)
    d = dominanceMain(p, f)
    print(d)

