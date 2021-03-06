from simulation.WaterQualitySim import WaterQualitySim
from simulation.WaterQualitySimData import WaterQualitySimData
from finalMain import SensorPlacement
from simulation.IndexToNode import index_to_node
from example.example2 import water_quality_simulation


# 处理节点重要性3000节点集的模拟

def data_process():
    """
    数据处理
    """
    sim_data_path = "F://AWorkSpace//2020data//3000节点组合json//CS-ec.json"  # 当前路径
    # 生成的文件名为：final_json.json
    WaterQualitySimData(json_path=sim_data_path).change_number(is_out=True)


def NSGA2():
    """
    算法迭代
    """
    wqs = WaterQualitySim("F:/AWorkSpace/Python-Learning-Data/cs11021.inp")

    final_json = "F://AWorkSpace//2020data//3000节点组合json//CS-pg-final.json"
    sp = SensorPlacement(json_path=final_json, individuals_num=200, iterations_num=500,
                         cross_probability=0.5,
                         mutation_probability=0.4)
    node_result = sp.iteration()  # 迭代主程序，输出结果
    sp.draw_node(node_result)  # 绘图
    #result_list = index_to_node(node_result, wqs.nodeList)  # 还原原来的节点名称
    #for i in result_list:
        #print(i)


def ky2_test():
    ky2 = "F:/AWorkSpace/Python-Learning-Data/ky2.inp"
    water_quality_simulation(ky2)

    """
       数据处理
       """
    #sim_data_path = "F://AWorkSpace//2020data//3000节点组合json//ky-ec.json"  # 当前路径
    # 生成的文件名为：final_json.json
    #WaterQualitySimData(json_path=sim_data_path).change_number(is_out=True)


if __name__ == "__main__":
    Net3_inp = "Net3.inp"
    # water_quality_simulation(Net3_inp)
    # data_process()
    NSGA2()
    #ky2_test()