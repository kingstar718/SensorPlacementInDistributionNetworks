# encoding:utf-8
import pandas as pd
import wntr
import os

class FilterNode():
    def __init__(self, inp_file):
        self.inp_file = inp_file
        self.wnModel = wntr.network.WaterNetworkModel(self.inp_file)

    def compute_water_data(self):
        wn = wntr.network.WaterNetworkModel(self.inp_file)
        sim = wntr.sim.EpanetSimulator(wn)
        wn.options.time.duration = 24 * 3600  # 设置水力时间为24小时
        result = sim.run_sim()  # 注意 所有的run_sim函数中的file_prefix参数需设置路径, 不然管网太大会生成三个大文件, 无法上传至github

        water_data = pd.DataFrame()     # 收集数据的pandas类,
        water_data["node_name"] = wn.node_name_list
        demand = result.node['demand']
        pressure = result.node['pressure']
        demand_list, pressure_list = [],[]
        for i in wn.node_name_list:
            diff_demand = self.diff_cal(demand[i])
            diff_pressure= self.diff_cal(pressure[i])
            demand_list.append(diff_demand)
            pressure_list.append(diff_pressure)
        water_data["diff_demand"] = demand_list
        water_data["diff_pressure"] = pressure_list

        ave_diameter, diff_diameter, pipe_len_list, volume_list = [], [], [], []
        for i in wn.node_name_list:
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
        water_data["ave_diameter"] = ave_diameter
        water_data["diff_diameter"] = diff_diameter
        water_data["pipe_len_list"] = pipe_len_list
        water_data["volume_list"] = volume_list

        # 度求解
        G = wn.get_graph()
        kv_degree = G.degree()
        degree_list = list(kv_degree.values())
        water_data["degree_list"] = degree_list
        """
        .ix is deprecated. Please use
        .loc for label based indexing or
        .iloc for positional indexing"""
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


if __name__ == "__main__":
    inp1 = "F:/AWorkSpace/Python-Learning-Data/Net3.inp"
    inp2 = "F:/AWorkSpace/Python-Learning-Data/ky8.inp"
    result = FilterNode(inp2).compute_water_data()
    path_or_buf = "D:\\Git\\SensorPlacementInDistributionNetworks\\simulation\\test.csv"
    # p = pd.read_csv(path_or_buf)
    # print(p)