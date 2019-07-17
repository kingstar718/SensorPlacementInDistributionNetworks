# encoding:utf-8
# 事件衍生算法雏形
from wntr import network, sim
from os import path, remove
from time import time
from WaterQualitySim import WaterQualitySim
import networkx

class EventDerivation(WaterQualitySim):
    def __init__(self, inp, is_simple=False):
        super().__init__(inp, is_simple)

    def init_model(self, time_duration=12 * 3600, report_time_step=600, report_start=0):
        time_duration = 16*3600
        return super().init_model(time_duration, report_time_step, report_start)

    def water_quality(self, node_name, start_time=0, end_time=12 * 3600, quality=10000,
                      rpt_file_path="F:\AWorkSpace\datatemp\ Node_"):
        start_time = 0
        end_time = 16*3600
        return super().water_quality(node_name, start_time, end_time, quality, rpt_file_path)

    def compute_derivation(self, node_name):
        water_quality = self.water_quality(node_name)
        node_list = list(water_quality.columns)
        index_list = list(water_quality.index)
        node_dirt = {}

        m_list =[]
        M_list =[]
        for i in node_list:
            time_list = []
            for n, j in enumerate(water_quality[i]):
                if j !=0:
                   time_list.append(index_list[n])
            if len(time_list)>0:
                M_list.append(i)
                node_dirt[i] = time_list[0]
            if len(time_list)>0 and time_list[0] <= 28800:
                m_list.append(i)
        print(len(m_list), len(M_list))
        print(m_list)
        print(M_list)
        print(self.init_model().junction_name_list)

        G = self.init_model().get_graph()
        G = G.to_directed()
        import wntr
        # wntr.graphics.plot_network(self.init_model(), node_attribute=M_list)
        for i in m_list:
            i_list = []
            for j in M_list:
                b = networkx.has_path(G, i, j)
                i_list.append(b)
            print("检查 %s 的连通性："%i ,i_list)
        print(node_dirt)
        for i in m_list:
            print(node_dirt[i])
            # print(time_list)

        return water_quality


if __name__ == "__main__":
    inp2 = "F:/AWorkSpace/Python-Learning-Data/ky2.inp"
    ed = EventDerivation(inp2)
    quality_data = ed.compute_derivation("J-135")