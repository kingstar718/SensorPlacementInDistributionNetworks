import os
import numpy as np
import pandas as pd

# 生成字典  节点污染模拟
def computeNodeDirt(filepath):
    fileList = os.listdir(filepath)
    NodeDirt = {}
    NodeList = []
    for i in range(len(fileList)):
        fileName = fileList[i]
        f = open(filepath+fileName, 'r')
        arr = []
        for lines in f.readlines():
            lines = lines.replace("\n", "").split(",")
            arr.append(lines)
        Dirt = {}
        for i in range(len(arr[0])):
            Dirt[arr[0][i]] = arr[1][i]
        #print(Dirt)
        NodeDirt[fileName[:len(fileName) - 4]] = Dirt
        NodeList.append(fileName[:len(fileName)-4])
        f.close()
    return  NodeDirt, NodeList


# 计算矩阵
def computeMatrix(NodeDirt, NodeList):
    nodeMatrix = []
    nodeDirt = {}

    for i,j in enumerate(NodeList):
        nodeDirt[j] =i   #i为索引 j为节点名称
    print(nodeDirt)
    count = 0
    for k in NodeDirt.values():
        l1 = [0] * len(NodeList)
        klist = list(k.keys())
        for j in NodeList:
            if j in klist:
                #print(nodeDirt[j], NodeDirt[i][k])
                l1[nodeDirt[j]] = int(k[j])
        nodeMatrix.append(l1)
        count = count+1
        print(count)
        #print(l1)
    #print(nodeMatrix)
    return nodeMatrix






if __name__=="__main__":
    file = 'F:\\AWorkSpace\\data\\DataCsDegree3\\'
    file2 = 'F:\\AWorkSpace\\data\\ky8_QualityData\\'
    dirtNode, nodelist  = computeNodeDirt(file)
    #print(dirtNode['10473'])
    print(nodelist)
    max = computeMatrix(dirtNode, nodelist)
    max = pd.DataFrame(max,index=None, columns=None)
    max.to_csv("max.csv", index=None, columns=None, header=False)

