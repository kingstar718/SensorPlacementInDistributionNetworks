from timematrix.commandline import command_line
from timematrix.splitfile import split_file
import re


#矩阵（列表）索引与实际的节点号之间的转换工具   根据索引值返回原来管网模型的节点编号
def index_to_node(repfilepath, nodeindex, regularmatch, nodeCount):
    nodelist = split_index(repfilepath, 0, regularmatch)
    onenodelist = nodelist[:nodeCount]
    return onenodelist[nodeindex-1]


def split_index(rptfilepath, qualindex, regularmatch):
    """
    :param filename: 报告文件路径
    :param qualindex: 节点的水质信息索引列号值
    :param regularmatch: 提取所有节点信息所需要的正则表达式
    :return: 当前节点在水力模拟时长内的每个报告时间点的水质信息list
    """
    f = open(rptfilepath,"r")
    filelist = f.readlines()
    waterqualitylist = []
    pattern = re.compile(regularmatch)    # 正则匹配 只选取有节点数据的行
    for line in filelist:
        str = line
        match = re.match(pattern, str, flags=0)
        if match:
            line = line.split( )    # 以空格区分一行内的字符串
            waterqualitylist.append(line[qualindex])     # 水质的索引列
    f.close()
    return waterqualitylist

if __name__ == "__main__":
    file1 = "F:/AWorkSpace/test/Net2node11.rpt"
    file2 = "F:/AWorkSpace/test/ky2node55.rpt"
    print(index_to_node(file1, 11, '  [0-9]', 36))
    print(index_to_node(file2, 55, '  J', 809))