import numpy as np

# 比较两个数组之间是否有相同元素的方法
list1 = [1,2,-1,4,5]
list2 = [11,3,12,6,7]
set1 = set(list1)
set2 = set(list2)
list3 = list(set1 & set2)
#print(list3.__len__())


def matchArray(list1, pop):
    l1 = []
    l2 = []
    for i in range(list1.shape[0]):
        if list1[i] >= 1:
            # print(1)
            l1.append(list1[i])  # 存节点的时间值
            l2.append(i)    # 存节点的索引
        else:
            l1.append(-1)
    s1 = set(l2)
    s2 = set(pop)
    s3 = np.array(list(s1&s2))    # 与传入的监测点组进行比较 保留相同的索引
    s3Number = int(s3.shape[0])
    if s3Number <= 0:   # 判断与一组监测点是否有相同的，即选择的监测点组能不能被监测到当前节点
        return -1      # V人为设定空的返回-1
    else:
        l3 = []
        for i in s3:    # s3保存的是相同的监测节点的索引
            l3.append(list1[i])
        l3 = np.array(l3)
        t = l3.min()
        return t


# 测试函数  如下
if __name__ == "__main__":
    # matchArray 需要两个np数组
    p1 = np.array([0, 10, 0, 0, 14, 0, 5, 0, 7])  # 索引1 4 6 8节点能监测到0（假设0为污染注入点）
    p2 = np.array([2, 4, 6])
    print(matchArray(p1, p2))    # 其中4 6 能监测到该节点，返回其中较小的索引6存储的时间5
