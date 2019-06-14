# !/usr/bin/env python
# encoding:UTF-8
from function.funUserDefine import *
from selection.selection import selection
from crossover import crossover
from mutation import mutation
from dominance.dominanceMain import dominanceMain
from dominance.estimate import estimate
from population_init import population
import matplotlib.pyplot as plt
from json import load, loads, dump, dumps


class SensorPlacement():
    def __init__(self, json_path, pop_size=500, individuals_num=100,
                 cross_probability=0.8, mutation_probability=0.2, iterations_num=100):
        """
        初始化参数
        :param json_path: json数据位置
        :param pop_size: 种群规模
        :param individuals_num: 个体数量
        :param cross_probability: 交叉概率
        :param mutation_probability: 变异概率
        :param iterations_num: 迭代次数
        """
        self.pop_size = pop_size
        self.individuals_num = individuals_num
        self.cross_probability = cross_probability
        self.mutation_probability = mutation_probability
        self.iterations_num = iterations_num
        self.json_path = json_path

    def read_json(self):
        """
        读取json数据, 转换为dirt
        :return: dirt数据
        """
        # jsonFile = "F:\\AWorkSpace\\Python-Learning-Data\\3628node2.json"
        with open(self.json_path, "r") as f:
            node_json = load(f)
        node_json = loads(node_json)
        return node_json

    def iteration(self):
        """
        算法迭代主程序
        :return: 最后迭代完成的排序,去重的种群
        """
        node_count  = len(self.read_json())
        pop = population(self.pop_size, self.individuals_num, node_count)
        node_dirt = self.read_json()
        func_obj = MinMax2(pop, node_dirt)

        for i in range(self.iterations_num):
            copy_pop = pop.copy()
            selection(pop, func_obj)
            crossover(pop, self.cross_probability)
            mutation(pop, self.mutation_probability, node_count-1)
            origin_pop = pop
            temp_pop = np.vstack((copy_pop, origin_pop))
            func_obj = MinMax2(temp_pop, node_dirt)
            pop = dominanceMain(temp_pop, func_obj)
            print("第 %d 次迭代" % i)

        # estimate(pop, func_obj)
        pop_node = np.array(list(set([tuple(sorted(t)) for t in pop])))      # 个体按数值大小排序, 去重
        return pop_node

    def draw_node(self, pop_result):
        for i in pop_result:
            print(i)
        list1 = []
        func_obj = MinMax2(pop_result, self.read_json())
        for i in func_obj.objFun_2():
            m = 1-i
            list1.append(m)
        # func_score = np.vstack((func_obj.objFun_1(), func_obj.objFun_2()))
        func_score = np.vstack((func_obj.objFun_1(), list1))
        np.set_printoptions(suppress=True)
        x = func_score[0]
        y = func_score[1]
        plt.scatter(x, y)
        plt.xlabel("min time")
        plt.ylabel("covered")
        plt.show()


if __name__ == '__main__':

    # 200个个体, 30个变量， 变量数值范围0到2**14
    # 交叉概率0.6， 编译概率0.1
    nodeCount1 = 3628
    jsonFile = "F:\\AWorkSpace\\Python-Learning-Data\\3628node2.json"
    jsonFile2 = "F:\\AWorkSpace\\data\\test\\final_json.json"   # 测试中json中的key和value中的list'内元素都为int
    sp = SensorPlacement(jsonFile2)

    node_result = sp.iteration()
    sp.draw_node(node_result)


