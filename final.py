from simulation.WaterQualitySim import WaterQualitySim
from simulation.WaterQualitySimData import WaterQualitySimData
from finalMain import SensorPlacement
from simulation.IndexToNode import index_to_node
from FilterNode import FilterNode
from WeightMain import WeightSensorPlacement


# 无文件形式
def dirt_test():
    ky8_inp = "F:/AWorkSpace/Python-Learning-Data/Net3.inp"
    wqs = WaterQualitySim(ky8_inp)      # 加载管网
    node_dirt = wqs.parallel_compute_time_dirt(wqs.nodeList, is_json=False)    # 水质模拟

    new_dirt = WaterQualitySimData(node_dirt=node_dirt).change_number(is_out=False)     # 数据处理

    sp = SensorPlacement(node_dirt=new_dirt, individuals_num=10, iterations_num=300)    # 算法迭代
    node_result = sp.iteration()        # 结果输出
    sp.draw_node(node_result)       # 帕累托解集显示
    result_list = index_to_node(node_result, wqs.nodeList)      # 将已转化为索引的节点再还原回来
    for i in result_list:
        print(i)
    print(node_dirt)
    print(new_dirt)


# 文件存储形式
def json_test():
    ky8_inp = "F:/AWorkSpace/Python-Learning-Data/Net3.inp"
    quality_path = "D:/Git/SensorPlacementInDistributionNetworks/simulation/"
    wqs = WaterQualitySim(ky8_inp)  # 加载管网
    wqs.parallel_compute_time_dirt(wqs.nodeList, rpt_file=quality_path)  # 水质模拟

    json_path = "D:/Git/SensorPlacementInDistributionNetworks/simulation/waterQuality.json"
    new_dirt = WaterQualitySimData(json_path=json_path).change_number(is_out=True)

    final_json = "D:/Git/SensorPlacementInDistributionNetworks/simulation/final_json.json"
    sp = SensorPlacement(json_path=final_json, individuals_num=10, iterations_num=500)      # 算法迭代
    node_result = sp.iteration()  # 结果输出
    sp.draw_node(node_result)  # 帕累托解集显示


def weight_test(inp):
    wqs = WaterQualitySim(inp)
    node_dirt = wqs.parallel_compute_time_dirt(wqs.nodeList, is_json=False)  # 水质模拟
    new_dirt = WaterQualitySimData(node_dirt=node_dirt).change_number(is_out=False)  # 数据处理

    # 权重数据
    fn = FilterNode(inp)
    data1 = fn.compute_water_data()
    data2 = fn.data_normalization(data1)
    print("管网节点数：", len(wqs.nodeList))
    print("污染数据的键数：", len(new_dirt.keys()))
    print(len(data2["diff_demand"]))
    pipe_list = list(data2["volume_list"])
    #print(len(pipe_list))
    for i, j in enumerate(new_dirt.values()):
        j.append(pipe_list[i])
    print(new_dirt)
    sp = WeightSensorPlacement(node_dirt=new_dirt, individuals_num=10, iterations_num=300)    # 算法迭代
    node_result = sp.iteration()  # 结果输出
    sp.draw_node(node_result)  # 帕累托解集显示
    result_list = index_to_node(node_result, wqs.nodeList)  # 将已转化为索引的节点再还原回来
    for i in result_list:
        print(i)


if __name__ == "__main__":
    inp1 = "F:/AWorkSpace/Python-Learning-Data/Net3.inp"
    inp2 = "F:/AWorkSpace/Python-Learning-Data/ky8.inp"
    inp3 = "F:/AWorkSpace/Python-Learning-Data/cs11021.inp"

    # weight_test(inp1)
    dirt_test()