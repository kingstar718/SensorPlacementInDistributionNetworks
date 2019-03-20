from commandline import command_line
from splitfile import split_file
from generatetimelist import generate_timelist
import numpy as np
import pandas as pd


def generate_timematrix(exepath, inpath, rptpath, sourcequality, duration, qual_reportstep, qualindex, regularmatch, nodeCount):
    """
    生成时间监测矩阵的函数
    :param exepath: EPANET的exe文件路径
    :param inpath: np管网模型文件路径
    :param rptpath: 输出报告文件路径
    :param sourcequality: 污染物注入数，单位mg
    :param duration: 水力模拟时长，单位s
    :param qual_reportstep:  水质模拟以及报告的间隔时长，单位s
    :param qualindex: 节点的水质信息索引列号值
    :param regularmatch: 提取所有节点信息所需要的正则表达式
    :param nodeCount:  管网模型总的节点数
    :return: 时间监测矩阵
    """
    timematrix = []
    for nodenum in range(nodeCount):
        nodenum = nodenum + 1
        command_line(exepath, inpath, rptpath, nodenum, sourcequality, duration, qual_reportstep)
        waterqualitylist = split_file(rptpath, qualindex, regularmatch)
        timelist = generate_timelist(waterqualitylist, nodenum, nodeCount, duration, qual_reportstep)
        timematrix.append(timelist)
        print("第 " ,nodenum, " 次生成时间矩阵")
    timematrix = np.array(timematrix)
    test = pd.DataFrame(data=timematrix)
    test.to_csv('test.csv', encoding='utf8',header=0,index=0)
    return timematrix


if __name__ == "__main__":
    exe1 = "D:/迅雷下载/EPANETDEMO.exe"
    input1 = "D:/迅雷下载/Net2.inp"
    rpt1 = "D:/迅雷下载/Net2.rpt"
    sourcequality1 = 200000  # 投入的污染物mg数
    duration1 = 10800  # 水力模拟时间参数
    qual_reportstep1 = 600  # 水质步长与报告间隔时间
    qualindex1 = 4
    regularmatch1 = '  [0-9]'
    nodeCount1 = 36
    #net2_matrix1 = generate_timematrix(exe1,input1,rpt1,sourcequality1,duration1,qual_reportstep1,qualindex1,regularmatch1,nodeCount1)
    #print(net2_matrix1)

    exe2 = "D:/迅雷下载/EPANETDEMO.exe"
    input2 = "D:/迅雷下载/ky2.inp"
    rpt2 = "D:/迅雷下载/ky2.rpt"
    sourcequality2 = 200000  # 投入的污染物mg数
    duration2 = 10800  # 水力模拟时间参数
    qual_reportstep2 = 600  # 水质步长与报告间隔时间
    qualindex2 = 4
    regularmatch2 = '  J'
    nodeCount2 = 809
    net2_matrix2 = generate_timematrix(exe2, input2, rpt2, sourcequality2, duration2, qual_reportstep2, qualindex2, regularmatch2, nodeCount2)
    print(net2_matrix2)