import os


def command_line(exepath, inpath, rptpath, nodenum, sourcequality, duration, qual_reportstep):
    '''
    :param exepath: EPANET的exe文件路径
    :param inpath: inp管网模型文件路径
    :param rptpath: 输出报告文件路径
    :param nodenum: 当前要模拟的节点数
    :param sourcequality: 污染物注入数，单位mg
    :param duration: 水力模拟时长，单位s
    :param qual_reportstep: 水质模拟以及报告的间隔时长，单位s
    :return: 报告文件，路径由rptpath设置
    '''
    # 需要将cmd命令写成如下形式   数值需要转化
    m = exepath+" "+inpath+" "+rptpath+" "+str(nodenum) + " " + str(sourcequality) + " " + str(duration) + " " +str(qual_reportstep)
    os.system(m)


if __name__ == "__main__":

    exe = "EPANETDEMO.exe"
    input = "Net2.inp"
    rpt = "out.rpt"
    node = 11


    exe1 = "D:/迅雷下载/EPANETDEMO.exe"
    input1 = "D:/迅雷下载/ky2.inp"
    rpt1 = "D:/迅雷下载/ky2.rpt"
    node1 = 55
    sourcequality = 200000  # 投入的污染物mg数
    duration = 10800  # 水力模拟时间参数
    qual_reportstep = 600  # 水质步长与报告间隔时间

    #command_line(exe1, input1, rpt1, node1,sourcequality,duration,qual_reportstep)

    command_line(exe,input,rpt,node,sourcequality,duration,qual_reportstep)

