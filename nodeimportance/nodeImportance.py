import wntr
import networkx as nx

"""
基于水力模型，结合NetworkX计算节点重要性
"""


class NodeImportance():
    """
    主函数，仅使用水力模型文件路径一个参数，计算相应的网络科学节点重要性几个参数
    """

    def __init__(self, inp_path=None):
        self.inp_path = inp_path

    def get_graph(self):
        return wntr.network.WaterNetworkModel(self.inp_path).get_graph()

    def betweenness_centrality(self, number=None):
        """介数中心性"""
        unsort_dirt = nx.betweenness_centrality(self.get_graph())
        return sort(unsort_dirt, number)

    def degree_centrality(self, number=None):
        """度中心性"""
        unsort_dirt = nx.degree_centrality(self.get_graph())
        return sort(unsort_dirt, number)

    def closeness_centrality(self, number=None):
        """接近中心性"""
        unsort_dirt = nx.closeness_centrality(self.get_graph())
        return sort(unsort_dirt, number)

    def eigenvector_centrality(self, number=None):
        """特征向量中心性"""
        unsort_dirt = nx.eigenvector_centrality(self.get_graph(), tol=100)
        return sort(unsort_dirt, number)

    def HITS(self, number=None):
        unsort_dirt = nx.hits(self.get_graph(), tol=100)  # 返回的是元组tuple
        unsort_dirt = dict(unsort_dirt[1])
        return sort(unsort_dirt, number)

    def page_rank(self, number=None):
        unsort_dirt = nx.pagerank(nx.DiGraph(self.get_graph()))  # 只能使用简单图
        return sort(unsort_dirt, number)

    def test(self):
        print(nx.current_flow_betweenness_centrality(nx.Graph(self.get_graph())))
        print(nx.current_flow_closeness_centrality(nx.Graph(self.get_graph())))
        print(nx.load_centrality(self.get_graph()))
        print(nx.katz_centrality(nx.Graph(self.get_graph())))


def sort(un_dirt, count=None):
    """
    根据k-v的v值排序k，并返回对应数量的key的list
    """
    if count is None:
        count = len(un_dirt.keys())
    return list(dict(sorted(un_dirt.items(), key=lambda e: e[1])).keys())[:count]


if __name__ == "__main__":
    Net3 = "D://Git//SensorPlacementInDistributionNetworks//example//Net3.inp"
    Ky2 = "F:\AWorkSpace\Python-Learning-Data\ky2.inp"
    cs = "F:\AWorkSpace\Python-Learning-Data\cs11021.inp"
    NI = NodeImportance(Ky2)
    bc = NI.betweenness_centrality()
    dc = NI.degree_centrality()
    cc = NI.closeness_centrality()
    ec = NI.eigenvector_centrality()
    hits = NI.HITS()
    page_rank = NI.page_rank()
    NI.test()
