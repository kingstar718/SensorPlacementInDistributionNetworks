from simulation.WaterQualitySim import WaterQualitySim
import wntr
import json

# 取出node的地址


def compute_xy(path):
    """
    存储所有node的xy坐标
    """
    wqs = wntr.network.WaterNetworkModel(path)
    node_list = wqs.node_name_list
    xy_dirt = {}
    for i in node_list:
        xy = wqs.get_node(i).coordinates
        xy_dirt.setdefault(i, xy)
    file_path = "F:/AWorkSpace/2020data/KY2Node_xy.json"
    with open(file_path, "w") as f:
        json.dump(xy_dirt, f)
    return wqs.get_node(node_list[0])


if __name__ == "__main__":
    cs = "F:\AWorkSpace\Python-Learning-Data\cs11021.inp"
    ky2 = "F:\AWorkSpace\Python-Learning-Data\ky2.inp"
    n = compute_xy(ky2)