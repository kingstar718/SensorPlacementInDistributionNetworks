from simulation.WaterQualitySim import WaterQualitySim
from time import time

def com_time(inp):
    wqs = WaterQualitySim(inp)

    nodeList = wqs.nodeList
    start = time()
    # node_dict = wqs.compute_time_dirt(nodeList, is_json=False)
    node_dict = wqs.parallel_compute_time_dirt(nodeList, parallel_num=10,is_json=False)
    print(time()-start)



if __name__ == "__main__":
    inp1 = "F:/AWorkSpace/Python-Learning-Data/Net3.inp"
    inp2 = "F:/AWorkSpace/Python-Learning-Data/ky2.inp"
    inp3 = "F:/AWorkSpace/Python-Learning-Data/ky8.inp"
    inp4 = "F:/AWorkSpace/Python-Learning-Data/cs11021.inp"
    com_time(inp2)