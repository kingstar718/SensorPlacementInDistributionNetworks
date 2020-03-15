import json


# 将各个节点重要性的结果输出出来


def read_json(path, centrality):
    """
    将各个节点重要性的3000个组成新的json
    """
    # 依据节点重要性的json文件，组成3000个节点
    with open(path, "r") as f:
        data = json.load(f)
    data = dict(data)
    # print(data[centrality])
    # print(len(data[centrality]))
    node_list = data[centrality]
    node_result_json = {}
    count = 0

    # 根据3000节点，从对应位置找到对应节点的模拟结果json文件，将其组合成一个大的json文件
    for i in node_list:
        json_path = "F://AWorkSpace//2020data//节点模拟结果数据//" + i + ".json"
        # print(json_path)
        with open(json_path, "r") as f:
            node_json = json.load(f)
            print(i)
            # print((node_json).get(i))
            print(dict(node_json).get(i))
            node_result_json.setdefault(i, dict(node_json).get(i))
        # count += 1
        # print("已完成：" + str(count))


    # 将最后的大json文件存储起来
    reslut_path = "F://AWorkSpace//2020data//3000节点组合json//CS-" + centrality + ".json"
    node_result_json = json.dumps(node_result_json)
    with open(reslut_path, "w") as f:
        json.dump(node_result_json, f)
    return node_result_json


if __name__ == "__main__":
    path = "F://AWorkSpace//2020data//节点重要性排序数据//node_centrality_cs_ec.json"
    d = read_json(path, "ec")