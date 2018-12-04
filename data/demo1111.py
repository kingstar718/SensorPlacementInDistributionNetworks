import pandas as pd
import numpy as np

filename = "net2report.csv"
# filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，
# header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。

np.set_printoptions(suppress=True)
df = pd.read_csv(filename,header=None,sep=",")

'''
list = []
for i in range(72):
    #print(i+1)
    list.append(i+1)
list = np.array(list)
print(list)
'''
p1 = np.array(df[0:2592])   # 第一个事件的所有污染事件
#print(p1)
'''
def splitArray(list,nodeNum):
    M = list.shape[0]
    N = nodeNum*6*12
    list = []
    for i in range(M//N):
        #print(i)
        l = np.array(df[(i*N):(i+1)*N])

        print(l)
        list.append(l)
    list = np.array(list)
    #print(list)

splitArray(df,36)
'''
# 生成节点编号与节点的第一个矩阵
def firstTimeArray(list):
    ll1 = []
    for i, j in enumerate(list):
        ls = []
        if j[1] != 0:
            ls.append(i)
            ls.append(j[0])
        else:
            continue
        ll1.append(ls)
    ll1 = np.array(ll1)
    return ll1

#lll = firstTimeArray(p1)
#print("lll",lll)


# 保留矩阵中第一次出现的list
def secondTimeArray(list):
    lls1 = []
    for i in range(list.shape[0]):
        for j in list:
            if (i + 1) == j[1]:
                j = j.tolist()
                lls1.append(j)
                break
    lls1 = np.array(lls1)
    return lls1


#lls = secondTimeArray(lll)
#print("lls",lls)
#a = np.zeros(36,dtype=int)
#print(a.shape[0])


# 判别污染事件各个节点最快监测到污染物的时间 传入参数为一个list
def countTime(list,a):
    for i in list:
        n = int(i[1]) - 1
        # print(n)
        if 0 <= i[0] <= 35:
            a[n] = 1
        elif 36 <= i[0] <= 71:
            a[n] = 10
        elif 72 <= i[0] <= 107:
            a[n] = 20
        elif 108 <= i[0] <= 143:
            a[n] = 30
        elif 144 <= i[0] <= 179:
            a[n] = 40
        elif 180 <= i[0] <= 215:
            a[n] = 50
        elif 216 <= i[0] <= 251:
            a[n] = 60
        elif 252 <= i[0] <= 287:
            a[n] = 70
        elif 288 <= i[0] <= 323:
            a[n] = 80
        elif 324 <= i[0] <= 359:
            a[n] = 90
        elif 360 <= i[0] <= 395:
            a[n] = 100
        elif 396 <= i[0] <= 431:
            a[n] = 110
        elif 432 <= i[0] <= 467:
            a[n] = 120
        elif 468 <= i[0] <= 503:
            a[n] = 130
        elif 504 <= i[0] <= 539:
            a[n] = 140
        elif 540 <= i[0] <= 575:
            a[n] = 150
        elif 576 <= i[0] <= 611:
            a[n] = 160
        elif 612 <= i[0] <= 647:
            a[n] = 170
        elif 648 <= i[0] <= 683:
            a[n] = 180
        elif 684 <= i[0] <= 719:
            a[n] = 190
        elif 720 <= i[0] <= 755:
            a[n] = 200
        elif 756 <= i[0] <= 791:
            a[n] = 210
        elif 792 <= i[0] <= 827:
            a[n] = 220
        elif 828 <= i[0] <= 863:
            a[n] = 230
        elif 864 <= i[0] <= 899:
            a[n] = 240
        elif 900 <= i[0] <= 935:
            a[n] = 250
        elif 936 <= i[0] <= 971:
            a[n] = 260
        elif 972 <= i[0] <= 1007:
            a[n] = 270
        elif 1008 <= i[0] <= 1043:
            a[n] = 280
        elif 1044 <= i[0] <= 1079:
            a[n] = 290
        elif 1080 <= i[0] <= 1115:
            a[n] = 300
        elif 1116 <= i[0] <= 1151:
            a[n] = 310
        elif 1152 <= i[0] <= 1187:
            a[n] = 320
        elif 1188 <= i[0] <= 1223:
            a[n] = 330
        elif 1224 <= i[0] <= 1259:
            a[n] = 340
        elif 1260 <= i[0] <= 1295:
            a[n] = 350
        elif 1296 <= i[0] <= 1331:
            a[n] = 360
        elif 1332 <= i[0] <= 1367:
            a[n] = 370
        elif 1368 <= i[0] <= 1403:
            a[n] = 380
        elif 1404 <= i[0] <= 1439:
            a[n] = 390
        elif 1440 <= i[0] <= 1475:
            a[n] = 400
        elif 1476 <= i[0] <= 1511:
            a[n] = 410
        elif 1512 <= i[0] <= 1547:
            a[n] = 420
        elif 1548 <= i[0] <= 1583:
            a[n] = 430
        elif 1584 <= i[0] <= 1619:
            a[n] = 440
        elif 1620 <= i[0] <= 1655:
            a[n] = 450
        elif 1656 <= i[0] <= 1691:
            a[n] = 460
        elif 1692 <= i[0] <= 1727:
            a[n] = 470
        elif 1728 <= i[0] <= 1763:
            a[n] = 480
        elif 1764 <= i[0] <= 1799:
            a[n] = 490
        elif 1800 <= i[0] <= 1835:
            a[n] = 500
        elif 1836 <= i[0] <= 1871:
            a[n] = 510
        elif 1872 <= i[0] <= 1907:
            a[n] = 520
        elif 1908 <= i[0] <= 1943:
            a[n] = 530
        elif 1944 <= i[0] <= 1979:
            a[n] = 540
        elif 1980 <= i[0] <= 2015:
            a[n] = 550
        elif 2016 <= i[0] <= 2051:
            a[n] = 560
        elif 2052 <= i[0] <= 2087:
            a[n] = 570
        elif 2088 <= i[0] <= 2123:
            a[n] = 580
        elif 2124 <= i[0] <= 2159:
            a[n] = 590
        elif 2160 <= i[0] <= 2195:
            a[n] = 600
        elif 2196 <= i[0] <= 2231:
            a[n] = 610
        elif 2232 <= i[0] <= 2267:
            a[n] = 620
        elif 2268 <= i[0] <= 2303:
            a[n] = 630
        elif 2304 <= i[0] <= 2339:
            a[n] = 640
        elif 2340 <= i[0] <= 2375:
            a[n] = 650
        elif 2376 <= i[0] <= 2411:
            a[n] = 660
        elif 2412 <= i[0] <= 2447:
            a[n] = 670
        elif 2448 <= i[0] <= 2483:
            a[n] = 680
        elif 2484 <= i[0] <= 2519:
            a[n] = 690
        elif 2520 <= i[0] <= 2555:
            a[n] = 700
        elif 2556 <= i[0] <= 2591:
            a[n] = 710
    return a
'''       
for i in range(72):
    i = i+1
    print("elif",(i-1)*36,"<=i[0]<=",i*36-1,":","a[n]=",(i-1)*10)
'''
# countTime(lls)


# 将其余为零的未检测到的事件设为水力模拟的时间
def changeZero(list, maxTime):
    for i in range(list.shape[0]):
        if list[i] == 0:
            list[i] = maxTime
#changeZero(a,720)
#print(a)


if __name__ == "__main__":
    M = df.shape[0]

    list_node = []
    for i in range(M//2592):
        a1 = np.zeros(36, dtype=int)
        l = np.array(df[i*2592:(i+1)*2592]).astype(np.int)     # 每2592个点是一次污染事件的全部模拟数据  取整
        l = firstTimeArray(l)   # 第一次求出各个污染事件发生时所有节点监测到污染的时间的list [list编号 节点id]
        l = secondTimeArray(l)  # 第二次求出污染事件发生时各节点最短监测到污染发生的时间list [list编号 节点id]
        a1 = countTime(l, a1)    # 根据[list编号 节点id] 中的list编号算出节点发生污染的时间
        changeZero(a1, 720)      # 未检测到污染的设置为水力模拟时长720分钟
        list_node.append(a1)
    list_node = np.array(list_node)
    #print(list_node)
    #print(list_node.shape[0])
    test = pd.DataFrame(data=list_node)
    print(test)
    #test.to_csv('f:/test.csv', encoding='utf8')

