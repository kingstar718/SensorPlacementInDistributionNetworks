from simulation.WaterQualitySim import WaterQualitySim
from simulation.WaterQualitySimData import WaterQualitySimData
from finalMain import SensorPlacement
from simulation.IndexToNode import index_to_node

"""
无文件形式只是很直观，但管网规模比较大时，多节点水质模拟、数据处理、算法迭代耗时都不短
因此函数还设计了分离模式，每个模块可以读上一个模块数据，生成为下一个模块使用的数据

步骤仍然是：水质模拟->数据处理->算法迭代
"""


def water_quality_simulation(inp_file):
    """
    水质模拟
    """
    wqs = WaterQualitySim(inp_file) # 加载管网
    sim_data_path = "example"  # 当前路径
    # 文件名为 examplewaterQuality.json
    wqs.parallel_compute_time_dirt(wqs.nodeList, rpt_file=sim_data_path)


def data_process():
    """
    数据处理
    """
    sim_data_path = "examplewaterQuality.json"  # 当前路径
    # 生成的文件名为：final_json.json
    WaterQualitySimData(json_path=sim_data_path).change_number(is_out=True)


def NSGA2():
    """
    算法迭代
    """
    wqs = WaterQualitySim("F:/AWorkSpace/Python-Learning-Data/Net3.inp")

    final_json = "final_json.json"
    sp = SensorPlacement(json_path=final_json, individuals_num=10, iterations_num=20)
    node_result = sp.iteration()  # 迭代主程序，输出结果
    sp.draw_node(node_result)  # 绘图
    result_list = index_to_node(node_result, wqs.nodeList)  # 还原原来的节点名称
    for i in result_list:
        print(i)


if __name__ == "__main__":
    Net3_inp = "Net3.inp"
    # water_quality_simulation(Net3_inp)
    # data_process()
    NSGA2()