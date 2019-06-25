#!/usr/bin/env python
#encoding:UTF-8
from random import sample, shuffle
from numpy import transpose, vstack


def mycmp2(i,  j, fun_score):
    """
    二元锦标赛 方式选择
    :param i:
    :param j:
    :param fun_score:
    :return:
    """
    s1 = 0
    s2 = 0
    s = fun_score.shape[1]

    for k in range(s):
        if fun_score[i][k] < fun_score[j][k]:
            s1+=1
        elif fun_score[i][k] > fun_score[j][k]:
            s2 += 1

    if s1 == 0 and s2 != 0:
        return j
    elif s1!= 0 and s2 == 0:
        return i
    else:
        temp = [i, j]
        shuffle(temp)
        return temp[0]
 

def selection(population, function_object):

    function_object.population=population       # 为函数对象赋值新的种群个体

    # 计算新种群目标函数数值，并建立矩阵 funScore
    func_score = vstack((function_object.objFun_1(), function_object.objFun_2()))
    func_score = transpose(func_score)
    #print(funScore)
    N=population.shape[0]
    V=population.shape[1]

    indicate_0 = range(N)
    indicate = []

    for _ in range(N):
        a1, a2 = sample(indicate_0, 2)
        indicate.append(mycmp2(a1, a2, func_score) )
    
    population[:] = population[indicate]
    func_score[:] = func_score[indicate]


if __name__ == "__main__":
    #np.random.seed(0)
    #random.seed(0)
    #from function.funUserDefine import *
    #population=np.random.rand(5, 2)
    #functionObject=ZDT1(population)
    #print(population)
    #print(functionObject)
    #selection(population, functionObject)
    #print(population)
    #print(functionObject)
    pass
