# encoding:utf-8
import pandas as pd
import wntr
import os
import numpy as np


class FilterNode():
    def __init__(self, inp_file):
        self.inp_file = inp_file
        self.wnModel = wntr.network.WaterNetworkModel(self.inp_file)

    def compute_water_data(self, to_csv = False):
        wn = wntr.network.WaterNetworkModel(self.inp_file)
        sim = wntr.sim.EpanetSimulator(wn)
        wn.options.time.duration = 24 * 3600  # 设置水力时间为24小时
        result = sim.run_sim()  # 注意 所有的run_sim函数中的file_prefix参数需设置路径, 不然管网太大会生成三个大文件, 无法上传至github

        water_data = pd.DataFrame()     # 收集数据的pandas类,
        water_data["node_name"] = wn.junction_name_list     # 改为只要junction点
        demand = result.node['demand']
        pressure = result.node['pressure']
        demand_list, pressure_list = [], []
        for i in wn.junction_name_list:     # 改为只要junction点
            diff_demand = self.diff_cal(demand[i])
            diff_pressure= self.diff_cal(pressure[i])
            demand_list.append(diff_demand)
            pressure_list.append(diff_pressure)
        water_data["diff_demand"] = demand_list
        water_data["diff_pressure"] = pressure_list

        ave_diameter, diff_diameter, pipe_len_list, volume_list = [], [], [], []
        for i in wn.junction_name_list:     # 改为只要junction点
            pipe_list = wn.get_links_for_node(i)
            dia_list, len_list, volume = [], [], []     # 存节点的管径,管长
            for j in pipe_list:
                all_pipe = wn.pipe_name_list
                if j in all_pipe:
                    dia = wn.links._data[j].diameter
                    node_len = wn.links._data[j].length
                    dia_list.append(dia)    # 所有直径
                    len_list.append(node_len)   # 所有管长
                    volume.append(dia*dia*node_len)     # 所有容积
            dia_list = sorted(dia_list)
            if len(dia_list) <= 1:
                dia_diff = 0
            else:
                dia_diff = dia_list[len(dia_list)-1] - dia_list[0]
            if len(dia_list) == 0:
                ave_dia = 0
            else:
                ave_dia = sum(dia_list)/(len(dia_list))
            pipe_len = sum(len_list)
            volume_node = sum(volume)
            # 将数据添加到list中
            ave_diameter.append(ave_dia)
            diff_diameter.append(dia_diff)
            pipe_len_list.append(pipe_len)
            volume_list.append(volume_node)
            print("节点%s 完成" % i)
        water_data["ave_diameter"] = ave_diameter
        water_data["diff_diameter"] = diff_diameter
        water_data["pipe_len_list"] = pipe_len_list
        water_data["volume_list"] = volume_list

        # 度求解
        G = wn.get_graph()
        kv_degree = G.degree()
        degree_list = list(kv_degree.values())
        water_data["degree_list"] = degree_list[0: len(wn.junction_name_list)]      # 改为只要junction点
        """
        .ix is deprecated. Please use
        .loc for label based indexing or
        .iloc for positional indexing"""
        if to_csv is True:
            water_data.to_csv(path_or_buf="test.csv")

        # 删掉生成的文件
        os.remove("temp.bin")
        os.remove("temp.inp")
        os.remove("temp.rpt")
        return water_data

    @staticmethod
    def diff_cal(sort_list):
        """
        计算列表最大值与最小值的绝对值
        :param sort_list:
        :return:
        """
        sort_list = sorted(sort_list)
        list_len = len(sort_list)
        return abs(sort_list[0] - sort_list[list_len-1])

    @staticmethod
    def data_normalization(pandas_data=None, to_csv=False, csv_path=None):
        """
        pandas数据的归一化，即值/和
        :param pandas_data: dataframe数据
        :param to_csv   是否保存为csv
        :param csv_path csv文件路径
        :return: new pandas_data
        """
        if pandas_data is None:
            node_data = pd.read_csv(csv_path)
        else:
            node_data = pandas_data
        node_data = node_data[
            ["diff_demand", "diff_pressure", "ave_diameter", "diff_diameter", "pipe_len_list", "volume_list",
             "degree_list"]]
        new_data = pd.DataFrame()
        for i in node_data:
            result_data = node_data[i] / node_data[i].sum()
            new_data[i] = result_data
        if to_csv is True:
            node_data.to_csv(path_or_buf="normalization.csv")
        return new_data

    @staticmethod
    def data_evaluation(pandas_data = None, csv_path = None):
        """
        使用收集的数据进行权重的求解
        :param pandas_data:  数据输入
        :param csv_path csv文件的路径
        :return:
        """
        if csv_path is None:
            p = pandas_data
        else:
            p = pd.read_csv(csv_path)
        zhibiao = ["diff_demand", "diff_pressure", "ave_diameter", "diff_diameter", "degree_list"]
        p = p[zhibiao]
        npl = p.values
        phalanx = np.dot(npl.T, npl)
        a, b = np.linalg.eig(phalanx)
        b2 = b.T
        weights_list = []
        for i in b2[0]:     # 权重为第一行
            weight = i/sum(b2[0])
            weights_list.append(weight)
        print("拉开档次法计算出来的权重：", weights_list)
        np.set_printoptions(suppress=True)
        for i in zhibiao:
            m = p[i]
            print(i,"的均方差为",'{:.8f}'.format(m.std()))

        '''
        evaluation_result = p["diff_demand"] * weights_list[0] + \
                            p["diff_pressure"] * weights_list[1] + \
                            p["ave_diameter"] * weights_list[2] + \
                            p["diff_diameter"] * weights_list[3] + \
                            p["degree_list"]*weights_list[4]
        print(evaluation_result)
        print(type(evaluation_result))'''

    @staticmethod
    def entropy_evaluation(pandas_data = None, csv_path = None):
        """
        熵值法
        默认数据已经经过无量纲化
        :param pandas_data:
        :param csv_path:
        :return:
        """
        if csv_path is None:
            p = pandas_data
        else:
            p = pd.read_csv(csv_path)
        zhibiao = ["diff_demand", "diff_pressure", "ave_diameter", "diff_diameter", "degree_list"]
        p = p[zhibiao]
        weight_list = []
        for i in zhibiao:
            m = p[i]
            list_data = list(m)
            #print(list_data)
            k = -1.0/np.log(len(list_data))
            value_sum = 0
            for i in list_data:     # 存在为0的值，需要设置一个极小值
                if i == 0:
                    i = 0.0001
                value = np.log(i)*i
                value_sum += value
            e = value_sum*k
            d = 1-e
            weight_list.append(d)
        # print(weight_list)
        result_list = []
        for i in range(len(weight_list)):       # 计算出的权重标准化
            m = weight_list[i]/sum(weight_list)
            result_list.append(m)
        print("拉开熵值法计算出来的标准化的权重：", result_list)

    @staticmethod
    def get_rank(pandas_data, sort_feature):
        """
        根据值获取索引series1[series1.values == 1].index
        根据索引获取值series1['a']
        :param pandas_data:
        :param sort_feature 表示根据哪个Series进行排序
        :return: 排序后的index列表
        """
        p = pandas_data[sort_feature]   # 取出要排序的Series
        p_name = pandas_data["node_name"]
        index_sort_list = p.sort_values(ascending=False).index      # 将排序后的索引拿出来
        node_list = []
        for i in index_sort_list:
            node_list.append(p_name[i])         # 根据索引将对应的节点名称存入新list
        return node_list


if __name__ == "__main__":
    inp1 = "F:/AWorkSpace/Python-Learning-Data/Net3.inp"
    inp2 = "F:/AWorkSpace/Python-Learning-Data/ky2.inp"
    inp3 = "F:/AWorkSpace/Python-Learning-Data/cs11021.inp"
    # result = FilterNode(inp2).compute_water_data()
    path_or_buf = "D:\\Git\\SensorPlacementInDistributionNetworks\\simulation\\test.csv"
    # p = pd.read_csv(path_or_buf)
    # print(p)
    csv_path1 = "F:/AWorkSpace/Python-Learning-Data/FilterNode/cs_normalization.csv"
    csv_path2 = "F:/AWorkSpace/Python-Learning-Data/FilterNode/cs_test.csv"

    fn = FilterNode(inp2)
    data1 = fn.compute_water_data()
    data2 = fn.data_normalization(pandas_data=data1)
    fn.data_evaluation(pandas_data=data2)
    fn.entropy_evaluation(pandas_data=data2)
    # node = fn.get_rank(data1, "degree_list")          # 根据值排序并得出以节点顺序存储
    # wn = wntr.network.WaterNetworkModel(inp3)