from waterqualitysim.WaterQualitySim import WaterQualitySim
from waterqualitysim.WaterQualitySimData import WaterQualitySimData
from finalMain import SensorPlacement
from waterqualitysim.IndexToNode import index_to_node


# 无文件形式
def dirt_test():
    ky8_inp = "F:/AWorkSpace/Python-Learning-Data/Net3.inp"
    wqs = WaterQualitySim(ky8_inp)      # 加载管网
    node_dirt = wqs.parallel_compute_time_dirt(wqs.nodeList, is_json=False)    #水质模拟
    new_dirt = WaterQualitySimData(node_dirt=node_dirt).change_number(is_out=False)     # 数据处理
    sp = SensorPlacement(node_dirt=new_dirt, individuals_num=10, iterations_num=100)    # 算法迭代
    node_result = sp.iteration()        # 结果输出
    sp.draw_node(node_result)       # 帕累托解集显示
    result_list = index_to_node(node_result, wqs.nodeList)
    for i in result_list:
        print(i)


# 文件存储形式
def json_test():
    ky8_inp = "F:/AWorkSpace/Python-Learning-Data/Net3.inp"
    quality_path = "D:/Git/SensorPlacementInDistributionNetworks/waterqualitysim/"
    wqs = WaterQualitySim(ky8_inp)  # 加载管网
    wqs.parallel_compute_time_dirt(wqs.nodeList, rpt_file=quality_path)  # 水质模拟

    json_path = "D:/Git/SensorPlacementInDistributionNetworks/waterqualitysim/waterQuality.json"
    new_dirt = WaterQualitySimData(json_path=json_path).change_number(is_out=True)

    final_json = "D:/Git/SensorPlacementInDistributionNetworks/waterqualitysim/final_json.json"
    sp = SensorPlacement(json_path=final_json, individuals_num=10, iterations_num=500)      # 算法迭代
    node_result = sp.iteration()  # 结果输出
    sp.draw_node(node_result)  # 帕累托解集显示


if __name__ == "__main__":
    inp1 = "F:/AWorkSpace/Python-Learning-Data/Net3.inp"
    inp2 = "F:/AWorkSpace/Python-Learning-Data/ky8.inp"
    inp3 = "F:/AWorkSpace/Python-Learning-Data/cs11021.inp"

    dirt_test()
