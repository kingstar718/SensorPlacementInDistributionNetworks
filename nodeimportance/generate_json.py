from nodeImportance import NodeImportance
import json

# 将各个指标筛选出来的3000个节点组成json

cs = "F:/AWorkSpace/Python-Learning-Data/cs11021.inp"
ky2 = "F:/AWorkSpace/Python-Learning-Data/ky2.inp"
ky8 = "F:/AWorkSpace/Python-Learning-Data/ky8.inp"


NI = NodeImportance(ky8)


def test1():
    bc = NI.betweenness_centrality()  # 耗时
    dc = NI.degree_centrality()
    cc = NI.closeness_centrality()
    ec = NI.eigenvector_centrality()
    hits = NI.HITS()
    page_rank = NI.page_rank()
    nx_dict = {}
    nx_dict.setdefault("bc", dc)
    nx_dict.setdefault("dc", dc)
    nx_dict.setdefault("cc", cc)
    nx_dict.setdefault("ec", ec)
    nx_dict.setdefault("hits", hits)
    nx_dict.setdefault("pg", page_rank)
    print(nx_dict)
    file_path = "F:/AWorkSpace/2020data/node_centrality_ky8.json"
    # print(file_path)
    with open(file_path, "w") as f:
        json.dump(nx_dict, f)
    print("存储完成！")


def test2():
    bc = NI.betweenness_centrality()  # 耗时
    '''
    ec = NI.eigenvector_centrality(3000)
    ex_dict = {}
    ex_dict.setdefault("ec",ec)
    file_path = "F:/AWorkSpace/2020data/node_centrality_cs_ec.json"
    # print(file_path)
    with open(file_path, "w") as f:
        json.dump(ex_dict, f)
    print("存储完成！")
    '''
    return bc


if __name__ == "__main__":
    # test1()
    test1()