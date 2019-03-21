# encoding:UTF-8
import os


def command_line(exepath, inpath, rptpath, nodenum, sourcequality, duration, qual_reportstep):
    """
    :param exepath: EPANET的exe文件路径
    :param inpath: inp管网模型文件路径
    :param rptpath: 输出报告文件路径
    :param nodenum: 当前要模拟的节点数
    :param sourcequality: 污染物注入数，单位mg
    :param duration: 水力模拟时长，单位s
    :param qual_reportstep: 水质模拟以及报告的间隔时长，单位s
    :return: 报告文件，路径由rptpath设置
    """
    # 需要将cmd命令写成如下形式   数值需要转化
    m = exepath+" "+inpath+" "+rptpath+" "+str(nodenum) + " " + str(sourcequality) + " " + str(duration) + " " +str(qual_reportstep)
    os.system(m)


if __name__ == "__main__":
    exe1 = "./test/EPANETDEMO.exe"
    input1 = "./test/Net2.inp"
    rpt1 = "./test/Net2.rpt"
    node1 = 11
    sourcequality1 = 200000  # 投入的污染物mg数
    duration1 = 10800  # 水力模拟时间参数
    qual_reportstep1 = 600  # 水质步长与报告间隔时间


    exe2 = "./test/EPANETDEMO.exe"
    input2 = "./test/ky2.inp"
    rpt2 = "./test/ky2.rpt"
    node2 = 55
    sourcequality2 = 200000  # 投入的污染物mg数
    duration2 = 10800  # 水力模拟时间参数
    qual_reportstep2 = 600  # 水质步长与报告间隔时间

    command_line(exe1, input1, rpt1, node1,sourcequality1, duration1, qual_reportstep1)

    command_line(exe2, input2, rpt2, node2, sourcequality2, duration2, qual_reportstep2)

