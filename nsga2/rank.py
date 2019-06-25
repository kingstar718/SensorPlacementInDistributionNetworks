#!/usr/bin/env python
#encoding:UTF-8
from copy import deepcopy


def rank(r_dict):
    """
    :param r_dict:  支配关系字典  {个体号码：[支配其的个数， 被其支配的个体列表]}
    :return: layer_dict: 分层字典   {1:[3,1,4], 2:[2,0]}
    """
    r_dict = deepcopy(r_dict)       # 拷贝 支配关系字典
    # 支配集分层, 层号初始化
    i = 1
    layer_dict = {}     # 分层字典 layer_dict

    while r_dict != {}:
        layer_dict[i] = []        # 取出当前种群非支配个体，放入第i层
        for k, v in r_dict.items():         # 找出当前非支配个体
            if v[0] == 0:
                layer_dict[i].append(k)
        for k in layer_dict[i]:     # 将被 第i层支配的个体 支配数减1
            # val[0] 支配 k 的个体数
            # val[1] 个体 k 支配的个体列表
            val = r_dict.pop(k)
            for v in val[1]:
                r_dict[v][0] -= 1
        i = i+1
    return layer_dict


if __name__ == "__main__":
    # r_dict={0: [7, []], 1: [3, [0, 2, 5]], 2: [6, [0, 5]], 3: [3, [0, 2, 5, 6]], 4: [0, [0, 1, 2, 3, 5, 6, 7, 8]],
    # 5: [8, []], 6: [5, [5]], 7: [3, [0, 2, 5, 6]], 8: [2, [0, 1, 2, 3, 5, 6, 7]], 9: [0, [0, 1, 2, 3, 5, 6, 7, 8]]}
    # print(rank(r_dict))
    from numpy import array
    funScore = array([[1, 2], [2, 2], [2, 2], [2, 2], [4, 3], [2, 1], [3, 1], [3, 2], [3, 3], [3, 4], [5, 6]])
    r = {0: [0, [1, 2, 3, 4, 7, 8, 9, 10]], 1: [2, [4, 7, 8, 9, 10]], 2: [2, [4, 7, 8, 9, 10]], 3: [2, [4, 7, 8, 9, 10]], 4: [8, [10]], 5: [0, [1, 2, 3, 4, 6, 7, 8, 9, 10]], 6: [1, [4, 7, 8, 9, 10]], 7: [6, [4, 8, 9, 10]], 8: [7, [4, 9, 10]], 9: [8, [10]], 10: [10, []]}
    print(rank(r))
'''
    from population_init import population
    from dominance1 import dominance
    import random
    p = population(10,2)
    m = fitness_pop(p)
    print(m)
    d = dominance(m)
    print(d)
    r = rank(d)
    print(r)
'''
"""
    输入：支配关系字典 r_dict
    {个体号码：[支配其的个数， 被其支配的个体列表]}

    输出:分层字典 layerDict
    {1:[3,1,4], 2:[2,0]}
"""