# coding:utf-8

import threading
import time
from splitfile import split_file
from  generatetimelist import generate_timelist
from commandline import command_line


class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__() # #注意：一定要显式的调用父类的初始化函数。
        self.arg = arg

    def run(self):
        time.sleep(1)
        print("MyThread the arg is : %s\r" % self.arg)

class EPAThread(threading.Thread):
    def __init__(self, node, nodeSum, infile):
        super(EPAThread, self).__init__() # #注意：一定要显式的调用父类的初始化函数。
        self.node = node
        self.nodeSum = nodeSum
        self.infile = infile


    def run(self ):
        exe1 = "F:/AWorkSpace/test/EPANETDEMO.exe"
        input1 = "F:/AWorkSpace/test/Net2.inp"
        outRpt = "F:/AWorkSpace/test/pare/node%d.rpt" % self.node
        command_line(exe1,input1, outRpt, self.node, 20000, 10800, 600)


        print(outRpt)

for i in range(4):
    t = EPAThread(i,4,4)
    t.start()

if __name__ == "__main__":
    '''
    file1 = "F:/AWorkSpace/test/Net2node11.rpt"
    file2 = "F:/AWorkSpace/test/ky2node55.rpt"
    list1 = split_file(file1, 4, '  [0-9]')
    list2= split_file(file2, 4, '  J')
    #print(np.array(list1))
    #print(np.array(list2))

    Net2node11_list = generate_timelist(list1, 11, 36, 10800, 600)
    ky2node55_list = generate_timelist(list2, 55, 809, 10800, 600)
    print(Net2node11_list)
    print(ky2node55_list)

    # Test1
    exe1 = "F:/AWorkSpace/test/EPANETDEMO.exe"
    input1 = "F:/AWorkSpace/test/Net2.inp"
    rpt1 = "F:/AWorkSpace/test/Net2node11.rpt"
    node1 = 11
    sourcequality1 = 200000  # 投入的污染物mg数
    duration1 = 10800  # 水力模拟时间参数
    qual_reportstep1 = 600  # 水质步长与报告间隔时间
    command_line(exe1, input1, rpt1, node1, sourcequality1, duration1, qual_reportstep1)
    '''