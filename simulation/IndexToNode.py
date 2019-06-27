# encoding:utf-8

def index_to_node(index_list, node_list):
    """
    将算法输出的索引结果转化为节点
    :param index_list:  算法输出的索引list
    :param node_list:  候选监测点节点编号list
    :return: 转换完成的list
    """
    node_dirt = {}
    for i, j in enumerate(node_list):
        node_dirt[i] = j
    result_list = []
    for i in index_list:
        temp_list = []
        for j in i:
            temp_list.append(node_dirt[int(j)])
        result_list.append(temp_list)
    return result_list