import json
import math

# 节点间编号的转换
class PreCross():
    def __init__(self, first_path, xy_path):
        self.first_path = first_path
        self.xy_path = xy_path
        self.index_node = self.read_node_json()
        self.xy_dict = self.read_xy()

    def read_node_json(self):
        """ 读取模拟数据文件，返回节点编号与index的dict """
        with open(self.first_path, "r") as f:
            data = json.load(f)
        d1 = json.loads(data)
        result_dict = {}
        for i, j in enumerate(d1.keys()):
            result_dict.setdefault(i, j)
        return result_dict

    def read_xy(self):
        """ 节点坐标数据读取"""
        with open(self.xy_path, "r") as f:
            data = json.load(f)
        return data

    def com_cross_point(self, node_list):
        point = 0
        for i in node_list:
            first_node = self.xy_dict[self.index_node[i]]
            for j in node_list:
                second_node = self.xy_dict[self.index_node[j]]
                length = math.sqrt((first_node[0]-second_node[0])*(first_node[0]-second_node[0])+
                                   (first_node[1]-second_node[1])*(first_node[1]-second_node[1]))
                point += length
        print(point/2)


if __name__ == "__main__":
    p1 = "F://AWorkSpace//2020data//3000节点组合json//ky8-1.json"
    p2 = "F://AWorkSpace//2020data//3000节点组合json//ky8-2.json"
    p3 = "F://AWorkSpace//2020data//3000节点组合json//CS-cc.json"
    p4 = "F://AWorkSpace//2020data//3000节点组合json//CS-cc-final.json"
    ky2xy = "F://AWorkSpace//2020data//节点坐标数据//KY2Node_xy.json"
    cs2xy = "F://AWorkSpace//2020data//节点坐标数据//CSNode_xy.json"
    Pr = PreCross(p3, cs2xy)
    Pr.com_cross_point([0, 1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
