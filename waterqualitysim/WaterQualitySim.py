# encoding:utf-8
from wntr import network, sim, morph
from time import time
from os import path, remove
from json import dump, dumps
from multiprocessing import Pool


class WaterQualitySim:
    """
    水质模拟类
    主要功能:
    初始化水力水质模型, 使用默认或重新设置的参数
    单节点污染模拟, 参数设置
    多节点污染模拟(串行/并行)
    """

    def __init__(self, inp, is_simple=False):
        self.inp_path = inp
        self.is_simple = is_simple
        # self.wn_model = self.init_model(self.is_simple)     # 管网模型对象
        if is_simple is False:
            self.wn_model = self.init_model()
        else:
            self.wn_model = self.simple_model()
        self.nodeList = self.wn_model.node_name_list  # 管网所有节点

    def init_model(self, time_duration=12 * 3600, report_time_step=600, report_start=0):
        """
        初始化管网模型
        :param time_duration: 水力时间
        :param report_time_step: 报告间隔
        :param report_start: 报告初始时间
        :return: wntr的管网对象
        """
        try:
            wn_model = network.WaterNetworkModel(self.inp_path)  # 加载管网inp文件
            for i in wn_model.node_name_list:
                wn_model.nodes._data[i]._initial_quality = 0  # 设置初始节点的水质都为0

                wn_model.options.quality.mode = 'CHEMICAL'  # 设置污染物为CHEMICAL
                wn_model.options.time.duration = time_duration  # 设置水力时间
                wn_model.options.time.report_timestep = report_time_step  # 设置报告间隔
                wn_model.options.time.report_start = report_start  # 设置报告初始时间
            return wn_model
        except:
            print("初始化管网模型发生异常")

    def simple_model(self):
        wn_model = self.init_model()
        simple_model = morph.skeletonize(wn_model, 400, return_map=False)
        return simple_model

    def water_quality(self, node_name, start_time=0, end_time=12 * 3600, quality=10000, rpt_file_path="F:\AWorkSpace\datatemp\ Node_"):
        """
        特定节点污染物注入模拟
        :param node_name: 节点名称
        :param start_time: 污染开始时间
        :param end_time: 污染结束时间
        :param quality: 污染注入克数
        :param rpt_file_path: 报告路径
        :return: 所有节点的间隔报告时间内的污染状况
        """
        try:
            start = time()
            # 设置源模式
            source_pattern = network.elements.Pattern.binary_pattern('SourcePattern',
                                                                          start_time=start_time,
                                                                          end_time=end_time,
                                                                          duration=self.wn_model.options.time.duration,
                                                                          step_size=self.wn_model.options.time.pattern_timestep)
            self.wn_model.add_pattern('SourcePattern', source_pattern)  # 添加模式
            self.wn_model.add_source('Source1', node_name, 'MASS', quality,
                               'SourcePattern')  # name, node_name, source_type, quality, pattern=None'     # 源注入的参数
            epanet_sim = sim.EpanetSimulator(self.wn_model)  # 加载wntr水力模型
            rpt = rpt_file_path + str(node_name)  # 设置输出文件位置
            epanet_sim_results = epanet_sim.run_sim(file_prefix=rpt)  # 水质模拟
            self.wn_model.remove_source('Source1')  # 除去现有源模式
            self.wn_model.remove_pattern('SourcePattern')  # 除去现有模式
            rpt_file = rpt + ".rpt"
            bin_file = rpt + ".bin"
            inp_file = rpt + ".inp"
            if path.exists(rpt_file) and path.exists(bin_file) and path.exists(inp_file):      # 计算完成, 删除目标文件
                remove(rpt_file)
                remove(bin_file)
                remove(inp_file)
            else:
                print("文件不存在")
            print("节点 %s 的污染模拟已完成" % node_name, "模拟用时: ", time() - start)
            return epanet_sim_results.node['quality']
        except:
            print("水质模拟发生异常")

    def compute_time(self, epa_data_frame):
        """
        从水质模拟结果计算污染事件发生 所有其他节点第一次发现污染的时间
        :param epa_data_frame: 某节点水质模拟结果
        :return: {节点名:  初次发生污染时间}
        """
        contamination_list = []
        # 将受到污染的节点拿出来
        for i in self.wn_model.node_name_list:
            if epa_data_frame.loc[43200, i] != 0:
                contamination_list.append(i)
        contamination_dirt = {}  # 键存节点名称 值存节点首次发生污染的时间
        for con_node in contamination_list:
            count = 0
            for quality in epa_data_frame[con_node]:
                if quality == 0:
                    count = count + 1
                else:
                    contamination_dirt[con_node] = count * 10
                    break
        return contamination_dirt

    # 主函数  从加载
    def compute_time_dirt(self, node_num_list, rpt_file="F:\AWorkSpace\data\ ", is_json=True):
        """
        计算管网所有事件的污染节点以及首次发生污染的时间
        :param node_num_list: 污染事件发生的节点集合
        :param rpt_file: 保存的文件路径
        :param is_json: 是否保存为json文件
        :return: 单个时间的csv文件, 所有事件的总的json文件
        """
        quality_dirt = {}
        for node_name in node_num_list:
            try:
                node_data_frame = self.water_quality(node_name)
                node_dirt = self.compute_time(node_data_frame)
                print(node_dirt)
                quality_dirt[node_name] = node_dirt  # 所有节点模拟的字典
            except:
                print("Node %s 发生异常" % node_name)
        # 将总的节点污染数据作为一个json文件存储起来
        if is_json is True:
            json_dirt = dumps(quality_dirt)
            json_file_name = rpt_file + "waterQuality.json"
            with open(json_file_name, "w") as f:
                dump(json_dirt, f)
        return quality_dirt

    def parallel_compute_time_dirt(self, node_num_list, rpt_file="F:\AWorkSpace\data\ ", parallel_num = 3, is_json=True):
        """
        计算管网所有事件的污染节点以及首次发生污染的时间
        :param node_num_list: 污染事件发生的节点集合
        :param rpt_file: 保存的文件路径
        :param parallel_num: 并行的进程数
        :param is_json: 单个时间的csv文件, 所有事件的总的json文件
        :return:
        """
        # 切分nodeList
        node_count = len(node_num_list)//parallel_num +10
        wn_list = [node_num_list[i:i + node_count] for i in range(0, len(node_num_list), node_count)]
        pool = Pool(processes=3)
        result = []
        for i in range(parallel_num):
            result.append(pool.apply_async(self.compute_time_dirt, (wn_list[i], rpt_file, False)))
        pool.close()
        pool.join()

        sum_dirt = {}
        for i in result:
            sum_dirt.update(i.get())     # 从并行里拿出结果并进行字典整合
        if is_json is True:
            json_dirt = dumps(sum_dirt)
            json_file_name = rpt_file + "waterQuality.json"
            with open(json_file_name, "w") as f:
                dump(json_dirt, f)
        return sum_dirt


if __name__ == "__main__":
    inp1 = "F:/AWorkSpace/Python-Learning-Data/Net3.inp"
    inp2 = "F:/AWorkSpace/Python-Learning-Data/ky8.inp"
    inp3 = "F:/AWorkSpace/Python-Learning-Data/cs11021.inp"
    wqs = WaterQualitySim(inp2 ,is_simple=True)
    start = time()
    simdort = wqs.parallel_compute_time_dirt(wqs.nodeList, is_json=False, parallel_num=3)
    print(time()-start)
    # 2 -- 44s
    # 3 - - 31s-35.5s-32.1s-31.7-31.7s
    # 4 -- 38s-38.8s-38.7s
    # 5 -- 38s
    # 6 -- 34s-32.48s-34.1s
    # 7 -- 30.9s-31.5s-30.9s-31.1s