# encoding:utf-8
# 事件衍生算法雏形
from wntr import network, sim
from os import path, remove
from time import time
from WaterQualitySim import WaterQualitySim
import networkx
import numpy as np
import pandas as pd
import json


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

    def compute_derivation(self, node_name, start_time, duration, is_json = False):
        """
        从主污染事件衍生次级事件
        :param node_name: 主事件节点名称
        :param start_time:  起始时间
        :param duration: 持续时间
        :param is_json 是否输出为json
        :return:
        """
        water_quality = self.water_quality(node_name)
        node_list = list(water_quality.columns)     # 其他节点
        index_list = list(water_quality.index)          # index为时间
        node_dirt = {}      # 当前节点污染事件影响的节点字典   {节点：初次污染的时间}

        m_list =[]      # 8小时时污染的节点集合
        M_list =[]      # 16小时污染的节点集合
        for i in node_list:
            time_list = []
            for n, j in enumerate(water_quality[i]):
                if j !=0:
                   time_list.append(index_list[n])
            if len(time_list)>0 and time_list[0] <=start_time+duration:
                M_list.append(i)
                node_dirt[i] = time_list[0]
            if len(time_list)>0 and time_list[0] <= start_time:
                m_list.append(i)

        #print(len(m_list), len(M_list))
        #print(m_list)
        #print(M_list)
        #print(self.init_model().junction_name_list)
        result_dirt = {}
        G = self.init_model().get_graph()
        G = G.to_directed()
        for i in m_list:
            i_list = []
            for j in M_list:
                b = networkx.has_path(G, i, j)      # 判断节点之间是否有路径    判断1
                if b is True:
                    i_list.append(j)    # 认为节点i发生的污染时间j能被波及
            i_dirt = {}

            for n in i_list:
                if node_dirt[i] < node_dirt[n]:
                    # 判断次级节点污染事件影响的节点在主事件的受到污染的时间是否要早  判断2
                    # 如果早了，则不是次级事件能影响到的节点
                    diff_time = int(node_dirt[n] - node_dirt[i])
                    if diff_time <= duration:
                        i_dirt[n] = diff_time
            i_dirt[i] = 600     # 将当前节点加入
            # print("当前节点是 %s " % i , node_dirt[i], i_dirt)
            result_dirt[i] = i_dirt
        if is_json is True:     # 保存为json文件
            result_json = json.dumps(result_dirt)
            with open(node_name+".json","w") as f:
                json.dump(result_json, f)
        return result_dirt


if __name__ == "__main__":
    inp2 = "F:/AWorkSpace/Python-Learning-Data/ky2.inp"
    ed = EventDerivation(inp2)
    result_list = quality_data = ed.compute_derivation("J-135", 28800, 28800)