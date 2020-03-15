import json
from finalMain import SensorPlacement
from simulation.IndexToNode import index_to_node
from simulation.WaterQualitySim import WaterQualitySim
from simulation.WaterQualitySimData import WaterQualitySimData


def read_paixu(json_path, cen, large):
    with open(json_path, "r") as f:
        node_json = json.load(f)
    return node_json[cen][:large]


def no_file(inp_path, cen, large):
    """
    不生成结果文件，数据全部由上个函数返回值组成
    """

    # 管网加载模块，改善自WNTR库，添加水质模拟模块
    wqs = WaterQualitySim(inp_path)

    # 水质模拟 is_json=False表示不产生json文件
    """
    产生dirt结果:
    {注入污染节点1：{影响节点1：初次污染时间，影响节点2：初次污染时间,...}，
     注入污染节点2：{影响节点1：初次污染时间，影响节点2：初次污染时间,...}，
     ...}
    """
    ky2_paixu = "F://AWorkSpace//2020data//节点重要性排序数据//node_centrality_ky2.json"
    node_list = read_paixu(ky2_paixu, cen, large)
    node_dirt = wqs.parallel_compute_time_dirt(node_list, is_json=False)
    # node_dirt = wqs.parallel_compute_time_dirt(wqs.nodeList, is_json=False)

    # 数据处理
    """
    将水质模拟的结果改为如下形式，并且节点映射为0 1 2 3...方便算法计算
    {节点1：[[污染事件1，污染事件2，...], 平均污染时间]，
     节点2：[[污染事件1，污染事件2，...], 平均污染时间]，
     ...}
    """
    dirt_data = WaterQualitySimData(node_dirt=node_dirt).change_number(is_out=False)

    # 算法计算
    sp = SensorPlacement(node_dirt=dirt_data, individuals_num=20, iterations_num=1000)

    # 迭代主程序 产生结果
    """
    node_result样式
    [[节点1，节点2..]
     [节点1，节点2..]
     ...]
    """
    node_result = sp.iteration()  # 迭代主程序，输出结果
    sp.draw_node(node_result)   # 绘图
    result_list = index_to_node(node_result, wqs.nodeList)  # 还原原来的节点名称
    for i in result_list:
        print(i)
    return node_result


def no_file2(inp_path):
    """
    不生成结果文件，数据全部由上个函数返回值组成
    """

    # 管网加载模块，改善自WNTR库，添加水质模拟模块
    wqs = WaterQualitySim(inp_path)

    # 水质模拟 is_json=False表示不产生json文件
    """
    产生dirt结果:
    {注入污染节点1：{影响节点1：初次污染时间，影响节点2：初次污染时间,...}，
     注入污染节点2：{影响节点1：初次污染时间，影响节点2：初次污染时间,...}，
     ...}
    """
    ky2_paixu = "F://AWorkSpace//2020data//节点重要性排序数据//node_centrality_ky2.json"
    # node_list = read_paixu(ky2_paixu, cen, large)
    #node_dirt = wqs.parallel_compute_time_dirt(node_list, is_json=False)
    node_dirt = wqs.parallel_compute_time_dirt(wqs.nodeList, is_json=False)

    # 数据处理
    """
    将水质模拟的结果改为如下形式，并且节点映射为0 1 2 3...方便算法计算
    {节点1：[[污染事件1，污染事件2，...], 平均污染时间]，
     节点2：[[污染事件1，污染事件2，...], 平均污染时间]，
     ...}
    """
    dirt_data = WaterQualitySimData(node_dirt=node_dirt).change_number(is_out=False)

    # 算法计算
    sp = SensorPlacement(node_dirt=dirt_data, individuals_num=100, iterations_num=500,
                         cross_probability=0.8,
                         mutation_probability=0.4)

    # 迭代主程序 产生结果
    """
    node_result样式
    [[节点1，节点2..]
     [节点1，节点2..]
     ...]
    """
    node_result = sp.iteration()  # 迭代主程序，输出结果
    sp.draw_node(node_result)   # 绘图
    result_list = index_to_node(node_result, wqs.nodeList)  # 还原原来的节点名称
    for i in result_list:
        print(i)
    return node_result


if __name__ == "__main__":
    # test('pg', 200)
    # ky2_test()
    ky2 = "F:/AWorkSpace/Python-Learning-Data/ky2.inp"
    ky8 = "F:/AWorkSpace/Python-Learning-Data/ky8.inp"
    # no_file(ky2, 'ec', 200)
    no_file2(ky2)
