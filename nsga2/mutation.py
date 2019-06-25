#!/usr/bin/env python
# encoding:UTF-8
from random import random, randint
from population_init import population
from copy import copy


def mutation(population, belta, max_num):
    old_population = copy(population)
    N = population.shape[0]
    V = population.shape[1]
    # print(V)

    for i in range(N):
        r = random()
        n = randint(0, V//2)    # 在个体的前半段随机选取一个点进行变异
        m = randint(V//2, V-1)  # 在个体的后半段随机选取一个点进行变异
        if r <= belta:
            if population[i][n]+1 <= max_num:
                population[i][n] = population[i][n]+1     # 整数编码,随机+1或者减1

            if population[i][m]-1 >= 0:
                population[i][m] = population[i][m]-1
    for i in range(N):
        m = len(set(population[i]))
        # print(m)
        if m < V:
            # print(population[i],old_population[i])
            population[i] = old_population[i]


# 以下是测试用例
if __name__ == "__main__":
    from numpy import random
    random.seed(0)
    xN = 5
    yN = 3
    belta = 1

    p=population(4, 7)
    print(p)
    mutation(p, belta, 29)
    print(p)
