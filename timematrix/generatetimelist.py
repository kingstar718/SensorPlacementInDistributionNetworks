# encoding:UTF-8
from splitfile import split_file
import numpy as np


# 将EPANET报告的水质信息生成矩阵
#exepath, inpath, rptpath, nodenum, sourcequality, duration, qual_reportstep
def generate_timelist(qwlist, nodenum, nodeCount, duration, qual_reportstep):
    '''
    将EPANET报告的水质信息生成矩阵
    :param qwlist: 由split_file函数生成的list，存储了当前模拟节点的所有其他节点在不同时间的水质信息
    :param nodenum: 当前发生污染的节点号
    :param nodeCount: 管网模型总节点数
    :param duration:  水力模拟时长
    :param qual_reportstep: 水质模拟与输出报告时长
    :return:
    '''
    rpttimes = int(duration/qual_reportstep)    # 报告次数
    # 行数=次数*节点数  nodetimelist    nodetimelist
    resultlist1 = [list() for i in range(nodeCount)]  # 初始的list1列表，保存所有节点的时间信息，每行为节点，列号为报告时间
    for i in range(rpttimes):
        demo_list = qwlist[i*nodeCount : (i+1)*nodeCount]  # 每隔nodeCount个节点即是一次报告时间内所有节点的数据
        timestep = int(qual_reportstep/60)*i # 将秒转换为分钟
        for k,v in enumerate(demo_list):
            if v!=0:
                resultlist1[k].append(timestep)
            else:
                resultlist1[k].append(0)
    resultlist1 = np.array(resultlist1)
    resultlist1[nodenum-1][0] = 1    # 污染注入节点时间设为1
    #resultlist1[nodenum ][0] = 1
    nodetimelist = [0]*nodeCount     # 最后返回的矩阵，即当前节点注入污染时，其他所有节点初次发现污染物的时间，未发现的设为0，也可设为水力时间
    count = 0
    for i in resultlist1:
        #i = np.array(i)
        if i.sum() != 0:    # 排除没有都到污染的节点
            for v in i:
                if v !=0:
                    nodetimelist[count] = v
                    break       # 找到不为0的值之后直接赋值返回， 即只取第一个不为0的值
        count = count + 1
    return nodetimelist

# 以下为初始编写demo，以一个具体的例子进行测试
#file = "out.rpt"
#l = split_file(file, 4, '  [0-9]')
#print(l)
def demo():
    result = [list() for i in range(36)]
    for i in range(18): # 不包括18
        demo_list=l[i*36:(i+1)*36]
        timestep = i*10
        for k,v in enumerate(demo_list):
            #print(k,v)
            if v!=0:
                result[k].append(timestep)
                #break
            else:
                result[k].append(0)
    result = np.array(result)
    result[10][0] = 1  # 污染注入节点时间设为1
    #print(result)
    resultlist2 = [0]*36
    count = 0
    for i in result:
        i = np.array(i)
        if i.sum() !=0:
            for v in i:
                if v!=0:
                    resultlist2[count] = v
                    break  # 找到不为0的值之后直接赋值返回
        count = count + 1
    #print(resultlist2)
    '''
    result2 = [list() for i in range(36)]
    for i, j in enumerate(result):
        print(i,j)
        for k in range(18):
            if j[k] !=0 and k < 18:
                result2[i].append(j[i])
                break
            else:
                result2[i].append(0)
    '''
    #print(result2)
'''
a = [2,3,4,1,2,4,2]
for i, j in enumerate(a):
    print(i,j)
'''
#demo()
'''
# 生成固定长度二维数组方法
a = [list() for i in range(5)]
a[0].append(1)
a[0].append(2)
a[1].append(3)
print(a)
'''

if __name__ == "__main__":
    file = "out.rpt"
    l = split_file(file, 4, '  [0-9]')
    t_list = generate_timelist(l,11,36,10800,600)
    print(t_list)
    #l2  =split_file("ky2.rpt",4,'  J')
    #t_lit2 = generate_timelist(l2,55,809,10800,600)
    #print(t_lit2)