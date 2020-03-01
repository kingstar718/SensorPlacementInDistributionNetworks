from nodeImportance import NodeImportance
from simulation.WaterQualitySim import WaterQualitySim
import json
import os


cs = "F:/AWorkSpace/Python-Learning-Data/cs11021.inp"
ky2 = "F:/AWorkSpace/Python-Learning-Data/ky2.inp"

NI = NodeImportance(ky2)

def test():
    # bc = NI.betweenness_centrality()  # 耗时
    dc = NI.degree_centrality(3000)
    cc = NI.closeness_centrality(3000)
    ec = NI.eigenvector_centrality(3000)
    hits = NI.HITS(3000)
    page_rank = NI.page_rank(3000)
    # NI.test()
    sum = set(dc+cc+ec+hits+page_rank)
    sum = list(sum)
    return sum

# 备注：各自的指标选取3000个节点，整合后不重复的节点共有7589个
# test()


def test2():
    csv_file = "F://水质监测点研究//2020新开始//7589csv.csv"
    with open(csv_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        first_line = lines[0]
        ss = first_line.split("', '")
    return ss


def test3():
    node_list = test2()
    wqs = WaterQualitySim(cs)
    new_node = []
    path = "F:/AWorkSpace/2020data/CSNodeJson/"
    new_list = test6(path)
    for i in node_list:
        if i not in new_list:
            new_node.append(i)

    print(len(new_node))
    print(new_node)
    simdort = wqs.parallel_compute_time_dirt(new_node[0:683], is_json=True, parallel_num=3)


def test4(path):
    """
    将整合的json文件分为单独的node-json文件
    """
    with open(path, "r") as f:
        data = json.load(f)
    d = json.loads(data)
    for i in d.keys():
        temp_dirt = {i:d.get(i)}
        # print(temp_dirt)
        file_path = "F:/AWorkSpace/2020data/CSNodeJson/" + i + ".json"
        # print(file_path)
        with open(file_path, "w") as f:
            json.dump(temp_dirt, f)
        print(i + "-存储完成！")
    return d


def test6(path):
    """
    检查文件夹内有多少已完成的node
    """
    node_list = os.listdir(path)
    new_list = []
    for i in node_list:
        l = i.split(".")
        new_list.append(l[0])
    return new_list


def test7(path):
    with open(path, "r") as f:
        data = json.load(f)
    d = json.loads(data)
    node_list = []
    for i in d.keys():
        node_list.append(i)
    print(len(node_list))


def simKy2():
    wqs = WaterQualitySim(ky2)
    simdort = wqs.parallel_compute_time_dirt(wqs.nodeList, is_json=True, parallel_num=3)


if __name__ == "__main__":
    json1 = "F:/AWorkSpace/2020data/waterQuality7.json"
    path = "F:/AWorkSpace/2020data/节点模拟结果数据/"
    # test3()
    # test4(json1)
    #s = test()
    #print(s)
    # simKy2()
    listtt = test6(path)