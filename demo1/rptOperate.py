import re
import numpy as np


# 对EPANET的报告文件进行的操作
def split_file(rptfilepath, qualindex, regularmatch):
    '''
    :param filename: 报告文件路径
    :param qualindex: 节点的水质信息索引列号值
    :param regularmatch: 提取所有节点信息所需要的正则表达式
    :return: 当前节点在水力模拟时长内的每个报告时间点的水质信息list
    '''
    f = open(rptfilepath,"r")
    filelist = f.readlines()
    waterqualitylist = []
    pattern = re.compile(regularmatch)    # 正则匹配 只选取有节点数据的行
    for line in filelist:
        str = line
        match = re.match(pattern, str, flags=0)
        if match:
            line = line.split( )    # 以空格区分一行内的字符串
            waterqualitylist.append(float(line[qualindex]))     # 水质的索引列
    np.set_printoptions(suppress=True)      # 取消科学计数法
    waterqualitylist = np.array(waterqualitylist)  # 转化为np矩阵
    f.close()
    return waterqualitylist

'''
def save_file(lister):      #  将传入的列表保存在新建文件中
    new_file = open('new.csv','w')      # 创建并打开文件，文件可写
    new_file.writelines(lister)     # 将列表lister中的内容逐行打印
    new_file.close()    # 关闭文件，且缓存区中的内容保存至该文件中
'''


if __name__ == "__main__":
    file = "out.rpt"
    l = split_file(file, 4, '  [0-9]')
    print(l)
    print(len(l))