# !/usr/bin/env python
# encoding:UTF-8
from function.funUserDefine import *
from selection import selection
from crossover import crossover
from mutation import mutation
from dominanceMain import dominanceMain
from estimate import estimate
from population_init import population
import matplotlib.pyplot as plt
from json import load, loads


class WeightSensorPlacement():
    def __init__(self, json_path=None, pop_size=500, individuals_num=100,
                 cross_probability=0.8, mutation_probability=0.2, iterations_num=100, is_file=True, node_dirt=None):
        """
        初始化参数
        :param json_path: json数据位置
        :param pop_size: 种群规模
        :param individuals_num: 个体数量
        :param cross_probability: 交叉概率
        :param mutation_probability: 变异概率
        :param iterations_num: 迭代次数
        :param is_file: 是否为文件读取
        :param node_dirt: 水质模拟的字典结果
        """
        self.pop_size = pop_size
        self.individuals_num = individuals_num
        self.cross_probability = cross_probability
        self.mutation_probability = mutation_probability
        self.iterations_num = iterations_num
        self.json_path = json_path
        self.node_dirt = node_dirt

    def read_json(self):
        """
        读取json数据, 转换为dirt
        :return: dirt数据
        """
        # jsonFile = "F:\\AWorkSpace\\Python-Learning-Data\\3628node2.json"
        if self.node_dirt is None:
            with open(self.json_path, "r") as f:
                node_json = load(f)
            node_json = loads(node_json)
        else:
            node_json = self.node_dirt
        return node_json

    def iteration(self):
        """
        算法迭代主程序
        :return: 最后迭代完成的排序,去重的种群
        """
        node_count  = len(self.read_json())
        pop = population(self.pop_size, self.individuals_num, node_count)
        node_dirt = self.read_json()
        func_obj = MinMax3(pop, node_dirt)

        for i in range(self.iterations_num):
            copy_pop = pop.copy()
            selection(pop, func_obj)
            crossover(pop, self.cross_probability)
            mutation(pop, self.mutation_probability, node_count-1)
            origin_pop = pop
            temp_pop = np.vstack((copy_pop, origin_pop))
            func_obj = MinMax3(temp_pop, node_dirt)
            pop = dominanceMain(temp_pop, func_obj)
            print("第 %d 次迭代" % i)

        # estimate(pop, func_obj)
        pop_node = np.array(list(set([tuple(sorted(t)) for t in pop])))      # 个体按数值大小排序, 去重
        return pop_node

    def draw_node(self, pop_result):
        #for i in pop_result:
            #print(i)
        list1 = []
        func_obj = MinMax3(pop_result, self.read_json())
        # estimate(pop_result, func_obj)
        for i in func_obj.objFun_2():
            m = 1-i
            list1.append(m)
        # func_score = np.vstack((func_obj.objFun_1(), func_obj.objFun_2()))
        func_score = np.vstack((func_obj.objFun_1(), list1))
        print(func_score)
        # funScore = np.transpose(func_score)
        np.set_printoptions(suppress=True)
        x = func_score[0]
        y = func_score[1]
        plt.scatter(x, y)
        plt.xlabel("min time")
        plt.ylabel("covered")
        plt.show()


if __name__ == "__main__":
    # 200个个体, 30个变量， 变量数值范围0到2**14
    # 交叉概率0.6， 编译概率0.1
    nodeCount1 = 3628
    jsonFile = "F:\\AWorkSpace\\Python-Learning-Data\\3628node2.json"
    jsonFile4 = "F:\\AWorkSpace\\Python-Learning-Data\\3628node3_weight.json"
    jsonFile2 = "F:\\AWorkSpace\\data\\test\\final_json.json"   # 测试中json中的key和value中的list'内元素都为int
    jsonFile3 = "F:\\AWorkSpace\\Python-Learning-Data\\DDirtnode3.json"
    sp = SensorPlacement(jsonFile4, iterations_num=500)
    node_result = sp.iteration()
    sp.draw_node(node_result)
    '''
    node_json = sp.read_json()
    print(len(node_json.values()))
    s = 0
    for i in node_json.values():
        s += i[4]
    print(s)
    
    for i in node_json.values():
        i[4] = i[4]/s
    m=0
    for i in node_json.values():
        m += i[4]
    print(m)
    import json
    node_json = json.dumps(node_json)
    with open(jsonFile4, "w") as f:
        json.dump(node_json, f)
    '''


    '''
    # 将权重加到原来的
    import json   
    with open(jsonFile, "r") as f:
        node_json = json.load(f)
    node_dirt = json.loads(node_json)
    weightfile= "F:\\AWorkSpace\\Python-Learning-Data\\json_node3628_weight.json"
    with open(weightfile, "r") as f:
        weight = json.load(f)
    weightlist = list(weight.values())
    for i in range(len(weightlist)):
        m = weightlist[i]/sum(weightlist)
        weightlist[i] = m
    '''
    '''
    for i, j in enumerate(node_dirt):
        node_dirt[str(i)].append(weightlist[i])
    jsonFile4 = "F:\\AWorkSpace\\Python-Learning-Data\\3628node3_weight.json"
    node_json = json.dumps(node_dirt)
    with open(jsonFile4, "w") as f:
        json.dump(node_json, f)
    '''

