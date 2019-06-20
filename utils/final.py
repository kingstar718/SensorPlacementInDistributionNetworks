from utils.WaterQualitySim import WaterQualitySim
from utils.WaterQualitySimData import WaterQualitySimData
from finalMain import SensorPlacement


if __name__=="__main__":
    inp1 = "F:/AWorkSpace/Python-Learning-Data/Net3.inp"
    inp2 = "F:/AWorkSpace/Python-Learning-Data/ky8.inp"
    inp3 = "F:/AWorkSpace/Python-Learning-Data/cs11021.inp"
    wqs = WaterQualitySim(inp1)
    node_dirt = wqs.parallel_compute_time_dirt(wqs.nodeList)
    new_dirt = WaterQualitySimData(node_dirt=node_dirt).change_number()
    print(len(new_dirt))

    sp = SensorPlacement(node_dirt=new_dirt, individuals_num=10, iterations_num=100)
    node_result = sp.iteration()
    sp.draw_node(node_result)