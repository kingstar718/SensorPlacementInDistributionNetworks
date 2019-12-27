from nodeImportance import NodeImportance
from simulation.WaterQualitySim import WaterQualitySim


cs = "F:/AWorkSpace/Python-Learning-Data/cs11021.inp"

NI = NodeImportance(cs)

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
    csv_file = "7589csv.csv"
    with open(csv_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        first_line = lines[0]
        ss = first_line.split("', '")
    return ss


def test3():
    node_list = test2()
    wqs = WaterQualitySim(cs)
    simdort = wqs.parallel_compute_time_dirt(node_list,is_json=False, parallel_num=3)
