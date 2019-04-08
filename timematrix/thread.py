#coding:utf-8

from splitfile import split_file
from  generatetimelist import generate_timelist

def threaddemo(nodeCount,startNode, endNode):
    pass



if __name__ == "__main__":
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