# encoding:utf-8
from json import load, loads, dump, dumps


class WaterQualitySimData():
    """
    水质模拟结果处理类
    主要流程:
    读取json文件
    节点与事件之间的装换
    先行计算所有节点能监测到的事件编号和平均监测时间
    将节点编号转换为index
    """
    def __init__(self, json_path=None, node_dirt=None):
        self.json_path = json_path
        self.node_dirt = node_dirt

    def read_node_json(self):
        """
        读取所有节点的污染数据 并转为dirt
        可选择使用json文件或者直接是dirt数据
        :return: node_dirt
        """
        if self.node_dirt is None:
            with open(self.json_path, "r") as f:
                node_json = load(f)
            node_dirt = loads(node_json)
            return node_dirt
        else:
            node_dirt = self.node_dirt
            return node_dirt

    def thing_node(self):
        """
        将之前的{事件: {节点: 时间, 节点: 时间, ...}}
        改为{节点: {事件: 时间, 事件: 时间}, ...}
        :return: 新的dirt
        """
        node_dirt = self.read_node_json()
        key_list = list(node_dirt.keys())
        new_dirt = {}
        for i in key_list:
            temp_dirt = {}
            for j in key_list:
                thing_list = list(node_dirt[j].keys())
                if i in thing_list:
                    thing_time = node_dirt[j][i]
                    temp_dirt[j] = thing_time
            new_dirt[i] = temp_dirt
            print("节点 %s 能监测到的事件已搜寻完成" % i)
        return new_dirt

    def compute_node(self, new_json_name="new_json.json", is_out=False):
        """
        先行计算所有节点能监测到的事件编号和平均监测时间
        :param: json文件路径
        :return:  json文件  包含所有节点的能监测到的事件编号和平均监测时间
        """
        # d = self.read_node_json()
        d = self.thing_node()    # j将其改为新的字典形式
        new_dirt = {}
        for i in d.keys():      # 所有节点编号
            l = []
            i_keys = list(d[i].keys())   # 当前节点的value中的下一级字典中的所有key键
            sum_time = 0
            for j in d[i].keys():
                sum_time = sum_time + int(d[i][j])
            if len(i_keys) != 0:
                average_time = sum_time / len(i_keys)
            else:
                average_time = 720  # 将无法监测到任何事件的节点的监测时间设为水力模拟时间720分钟
                # print("节点 %s 不能监测到任何事件" % i)
            l.append(i_keys)
            l.append(average_time)
            new_dirt[i] = l
            # print("节点 %s 已修改" % i)
        if is_out is True:
            new_json = dumps(new_dirt)
            with open(new_json_name, "w") as f:
                dump(new_json, f)
        return new_dirt

    def change_number(self, final_json="final_json.json", is_out=False):
        """
        将原字典里所有的使用节点编号的替换成index
        :return: final nodeDirt
        """
        change_dirt = {}    # 用于交换的字典, key为节点编号, value为索引
        node_dirt = self.compute_node()
        node_list = list(node_dirt.keys())
        for i, j in enumerate(node_list):
            change_dirt[j] = i

        final_dirt = {}
        d = node_dirt
        for i, j in enumerate(d.keys()):
            final_dirt[str(i)] = d[j]  # 新建字典, key为index, value为原来的nodeDirt的value
        for i in d.values():
            for j in range(len(i[0])):
                k = i[0][j]
                v = change_dirt[k]
                i[0][j] = v  # 将新字典里的values里第一个所有节点的编号改为index
        # print(newDirt)
        if is_out is True:
            new_json = dumps(final_dirt)
            with open(final_json, "w") as f:
                dump(new_json, f)
        return final_dirt


if __name__ == "__main__":
    json_path = "F:\\AWorkSpace\\data\\test\\waterQuality_ky8.json"
    json_path2 = "F:\\AWorkSpace\\Python-Learning-Data\\node.json"
    # 函数测试
    # wnsd = WaterQualitySimData(json_path)
    # nodeDirt = wnsd.change_number()
