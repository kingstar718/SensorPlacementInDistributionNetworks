import pandas as pd
import numpy as np
from demo1111 import *
filename = "net3.csv"

np.set_printoptions(suppress=True)
df = pd.read_csv(filename,header=None,sep=",")


def countTime1(list,a):
    for i in list:
        n = int(i[1]) - 1
        print(n)
        if 0 <= i[0] <= 96:
            a[n] = 0

        elif 97 <= i[0] <= 193:
            a[n] = 10

        elif 194 <= i[0] <= 290:
            a[n] = 20

        elif 291 <= i[0] <= 387:
            a[n] = 30

        elif 388 <= i[0] <= 484:
            a[n] = 40

        elif 485 <= i[0] <= 581:
            a[n] = 50

        elif 582 <= i[0] <= 678:
            a[n] = 60

        elif 679 <= i[0] <= 775:
            a[n] = 70

        elif 776 <= i[0] <= 872:
            a[n] = 80

        elif 873 <= i[0] <= 969:
            a[n] = 90

        elif 970 <= i[0] <= 1066:
            a[n] = 100

        elif 1067 <= i[0] <= 1163:
            a[n] = 110

        elif 1164 <= i[0] <= 1260:
            a[n] = 120

        elif 1261 <= i[0] <= 1357:
            a[n] = 130

        elif 1358 <= i[0] <= 1454:
            a[n] = 140

        elif 1455 <= i[0] <= 1551:
            a[n] = 150

        elif 1552 <= i[0] <= 1648:
            a[n] = 160

        elif 1649 <= i[0] <= 1745:
            a[n] = 170

        elif 1746 <= i[0] <= 1842:
            a[n] = 180

        elif 1843 <= i[0] <= 1939:
            a[n] = 190

        elif 1940 <= i[0] <= 2036:
            a[n] = 200

        elif 2037 <= i[0] <= 2133:
            a[n] = 210

        elif 2134 <= i[0] <= 2230:
            a[n] = 220

        elif 2231 <= i[0] <= 2327:
            a[n] = 230

        elif 2328 <= i[0] <= 2424:
            a[n] = 240

        elif 2425 <= i[0] <= 2521:
            a[n] = 250

        elif 2522 <= i[0] <= 2618:
            a[n] = 260

        elif 2619 <= i[0] <= 2715:
            a[n] = 270

        elif 2716 <= i[0] <= 2812:
            a[n] = 280

        elif 2813 <= i[0] <= 2909:
            a[n] = 290

        elif 2910 <= i[0] <= 3006:
            a[n] = 300

        elif 3007 <= i[0] <= 3103:
            a[n] = 310

        elif 3104 <= i[0] <= 3200:
            a[n] = 320

        elif 3201 <= i[0] <= 3297:
            a[n] = 330

        elif 3298 <= i[0] <= 3394:
            a[n] = 340

        elif 3395 <= i[0] <= 3491:
            a[n] = 350

        elif 3492 <= i[0] <= 3588:
            a[n] = 360

        elif 3589 <= i[0] <= 3685:
            a[n] = 370

        elif 3686 <= i[0] <= 3782:
            a[n] = 380

        elif 3783 <= i[0] <= 3879:
            a[n] = 390

        elif 3880 <= i[0] <= 3976:
            a[n] = 400

        elif 3977 <= i[0] <= 4073:
            a[n] = 410

        elif 4074 <= i[0] <= 4170:
            a[n] = 420

        elif 4171 <= i[0] <= 4267:
            a[n] = 430

        elif 4268 <= i[0] <= 4364:
            a[n] = 440

        elif 4365 <= i[0] <= 4461:
            a[n] = 450

        elif 4462 <= i[0] <= 4558:
            a[n] = 460

        elif 4559 <= i[0] <= 4655:
            a[n] = 470

        elif 4656 <= i[0] <= 4752:
            a[n] = 480

        elif 4753 <= i[0] <= 4849:
            a[n] = 490

        elif 4850 <= i[0] <= 4946:
            a[n] = 500

        elif 4947 <= i[0] <= 5043:
            a[n] = 510

        elif 5044 <= i[0] <= 5140:
            a[n] = 520

        elif 5141 <= i[0] <= 5237:
            a[n] = 530

        elif 5238 <= i[0] <= 5334:
            a[n] = 540

        elif 5335 <= i[0] <= 5431:
            a[n] = 550

        elif 5432 <= i[0] <= 5528:
            a[n] = 560

        elif 5529 <= i[0] <= 5625:
            a[n] = 570

        elif 5626 <= i[0] <= 5722:
            a[n] = 580

        elif 5723 <= i[0] <= 5819:
            a[n] = 590

        elif 5820 <= i[0] <= 5916:
            a[n] = 600

        elif 5917 <= i[0] <= 6013:
            a[n] = 610

        elif 6014 <= i[0] <= 6110:
            a[n] = 620

        elif 6111 <= i[0] <= 6207:
            a[n] = 630

        elif 6208 <= i[0] <= 6304:
            a[n] = 640

        elif 6305 <= i[0] <= 6401:
            a[n] = 650

        elif 6402 <= i[0] <= 6498:
            a[n] = 660

        elif 6499 <= i[0] <= 6595:
            a[n] = 670

        elif 6596 <= i[0] <= 6692:
            a[n] = 680

        elif 6693 <= i[0] <= 6789:
            a[n] = 690

        elif 6790 <= i[0] <= 6886:
            a[n] = 700

        elif 6887 <= i[0] <= 6983:
            a[n] = 710

    return a


if __name__ == "__main__":
    M = df.shape[0]

    list_node = []
    #print(M//6984)

    for i in range(M // 6984):
        a1 = np.zeros(97, dtype=int)
        l = np.array(df[i * 6984:(i + 1) * 6984])  # 每2592个点是一次污染事件的全部模拟数据  节点36*12*6=2592
        l = firstTimeArray(l)  # 第一次求出各个污染事件发生时所有节点监测到污染的时间的list [list编号 节点id]
        l = secondTimeArray(l)  # 第二次求出污染事件发生时各节点最短监测到污染发生的时间list [list编号 节点id]
        a1 = countTime1(l, a1)  # 根据[list编号 节点id] 中的list编号算出节点发生污染的时间
        changeZero(a1, 720)  # 未检测到污染的设置为水力模拟时长720分钟
        # print("第",i,"次",a1)
        list_node.append(a1)
        print("第",i,"次")
    list_node = np.array(list_node)
    #print(list_node)
    test = pd.DataFrame(data=list_node)
    #print(test)
    #test.to_csv('f:/test.csv', encoding='utf8')
