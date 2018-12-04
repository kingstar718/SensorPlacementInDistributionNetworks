

def countTime1(list,a):
    for i in list:
        n = int(i[1]) - 1
        #print(n)
        if 0 <= i[0] <= 808:
            a[n] = 1
        elif 809 <= i[0] <= 1617:
            a[n] = 10
        elif 1618 <= i[0] <= 2426:
            a[n] = 20
        elif 2427 <= i[0] <= 3235:
            a[n] = 30
        elif 3236 <= i[0] <= 4044:
            a[n] = 40
        elif 4045 <= i[0] <= 4853:
            a[n] = 50
        elif 4854 <= i[0] <= 5662:
            a[n] = 60
        elif 5663 <= i[0] <= 6471:
            a[n] = 70
        elif 6472 <= i[0] <= 7280:
            a[n] = 80
        elif 7281 <= i[0] <= 8089:
            a[n] = 90
        elif 8090 <= i[0] <= 8898:
            a[n] = 100
        elif 8899 <= i[0] <= 9707:
            a[n] = 110
    return a

def firstTimeArray1(list):
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


def secondTimeArray1(list):     # 此时的list是一个[index,编号]的形式
    lls1 = []
    for i in range(list.shape[0]):
        for j in list:
            if (i + 1) == j[1]:
                j = j.tolist()
                lls1.append(j)
                break
    lls1 = np.array(lls1)
    return lls1


def changeNode(list):      # 将编号由字符改为数值
    for j in range(18):
        for i in range(809):
            m = (j*809)+i   # 依次找出list的编号
            n = i+1     # 依次为0-808
            #print(m, n)
            list[m][0] = n
    return list

if __name__ == "__main__":
    from demo1111 import *

    filename = "F:/data/809809.csv"

    np.set_printoptions(suppress=True)
    df = pd.read_csv(filename, header=None, sep=",")
    # print(df)
    M = df.shape[0]
    '''
    # print(M)  # 14562
    l = np.array(df[0+14562:14562*2])
    l = changeNode(l)
    print(l)
    l1 = firstTimeArray1(l)
    l1 = secondTimeArray(l1)
    a = countTime1()
    print(l1)
    '''
    #print(l)
    list_node = []
    # print(M//14562)    # 809

    oneSimulate = 14562     # 一次模拟的行数
    nodeNum = 809

    for i in range(M // 14562):
        a1 = np.zeros(809, dtype=int)
        l = np.array(df[i * 14562:(i + 1) * 14562])  # 每2592个点是一次污染事件的全部模拟数据  节点36*12*6=2592
        l = changeNode(l)
        l = firstTimeArray(l)  # 第一次求出各个污染事件发生时所有节点监测到污染的时间的list [list编号 节点id]
        l = secondTimeArray(l)  # 第二次求出污染事件发生时各节点最短监测到污染发生的时间list [list编号 节点id]
        a1 = countTime1(l, a1)  # 根据[list编号 节点id] 中的list编号算出节点发生污染的时间
        changeZero(a1, 180)  # 未检测到污染的设置为水力模拟时长720分钟
        # print("第",i,"次",a1)
        list_node.append(a1)
        print("第", i, "次")
    list_node = np.array(list_node)
    #print(list_node)
    test = pd.DataFrame(data=list_node)
    print(test)
    test.to_csv('f:/test8091.csv', encoding='utf8')
