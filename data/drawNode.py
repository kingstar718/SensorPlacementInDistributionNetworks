import wntr
from timematrix.fileread import computeNodeDirt
import numpy as np

def drawnode(inp, nodeResult):
    wn = wntr.network.WaterNetworkModel(inp)
    wntr.graphics.plot_network(wn, title="nodepalce", node_attribute=nodeResult)


def indexTonode(nodeIndexList, nodeList):
    nodeResult = []
    for i in nodeIndexList:
        nodeResult.append(nodeList[i])
    return nodeResult


if __name__=="__main__":
    file = 'F:\\AWorkSpace\\data\\DataCsDegree3\\'
    file2 = 'F:\\AWorkSpace\\data\\ky8_QualityData\\'

    nodeindex = [ 163, 2110, 2841, 3343,  735, 1568, 2187, 1817,  915, 3430, 1427, 1402, 1799, 2302, 1802, 2209, 3441, 2908,  522,  179, 2895, 2785, 2738,  370 , 550 ,2712 ,1904, 1908, 3182 ,1082, 3271 ,1883 ,1650 , 403 ,1322, 1247,  983, 1329 ,2871 ,2760, 2252 ,1753, 2293,  972, 3377, 2870 ,3543,  719 ,3331, 3449]
    nodeindex2 = [2815,3154, 2378 , 482,   89, 1604 ,1070, 2412,  742, 240 ,2483, 1624, 2951 ,1387, 1057 ,3001, 2534 ,3443, 2911, 2972 ,1737, 2113,  508, 3610 ,1663, 1108, 1013,  694, 3598, 3117,  983,  710, 3161, 2187, 2507,  844, 2321,  929, 3430, 2754, 3489, 1145, 2195,  665, 2357,  913, 1039, 1610,  157, 1113]
    nodeindex3 = [3085 ,2766  ,624, 3577 ,1083, 2698 ,1088 ,1939 ,2423, 2719 ,2908 , 403, 2045 , 626 , 609, 3328 ,2353 ,3193,  697, 1488 ,1900 ,2157, 2753, 3512, 1031, 3219 ,1545, 2110,  936 ,1594 ,1840 ,1378,  611 , 751 ,2164 ,1852 ,2296,1225 ,1457 , 935 ,2616, 1823 ,3210, 3606,  985,  983, 3202, 2963 ,3297 ,2484, 2418,  885 ,1476 , 220 ,1883, 2523 ,3358 , 799,  566 ,1285 ,3433, 2018 ,2494  ,130 ,1612 ,1546 ,2524, 1073 ,2458 ,1992, 2488 , 951, 1970 ,2984, 3436, 1781, 2442, 1453, 2938 , 906]
    nodeindex4 = [3085 ,2766,  625 ,3577 ,1083 ,2698 ,1088 ,1939 ,2422 ,2719 ,2908 , 402, 2045  ,626 , 609 ,3328, 2353 ,3193 , 697 ,1488 ,1900, 2157 ,2753 ,3512 ,1031, 3219 ,1544, 2110,  936 ,1595, 1839 ,1378 , 611 , 751 ,2164 ,1852 ,2296 ,1225 ,1457 , 935  ,169, 2976 ,2808 ,3537 ,3621, 2235, 2266 , 389,  178 ,2259 ,3564 ,1630 ,1882,   95, 2122 ,1596, 3189, 1074 , 993 ,2928  ,509, 2569 ,3151,  331 ,1283, 2761,  450  ,848 ,3272,  319 ,3156, 2206 ,1525 ,3296 ,2905, 1687 , 724, 3472, 2887 , 310]
    nodeindex5 = [2757, 3265, 1407, 1400, 3430, 3529 , 476, 1857,  631, 3301, 2905,  601, 3625, 3444, 2444,  179,   91, 1655, 1910,  648, 2047, 3167,  232, 2499, 2382,  373, 1327, 1654, 2426, 2520, 3548, 2558, 1771, 2674, 2349,  534,   61, 1098,  469, 3120, 1060, 2659, 3035, 1960,  776, 1813, 2951, 2185, 1626, 1708]
    nodeindex6_300_120_30 = [2865, 1227, 3381, 2098, 2687, 1618,  696, 2908, 2603, 3136,  653,  586, 1707, 1851,  239, 1431, 2133, 2515,  944, 1779, 3089,  877, 1534, 1947,  362, 3248,   48, 2164, 2251,  941, 2866, 2962, 2855 ,2778 , 164  ,282 ,2567 , 185 ,1804 ,3258,  378 ,1022,  775,  900 , 764, 2838, 1965, 3320, 1532, 2794, 2826  ,758, 1095, 1169, 1780, 1937 ,2230 ,2489, 3400, 2390, 1310 ,2938, 2941, 669, 2530, 3225, 2927, 3175, 1770 ,2721 ,3123 , 671 , 814 ,3444 ,3606 ,2691 ,2622 ,3049, 3013, 2538, 1309 ,1123,  861, 1708, 1831, 2167 ,1619, 1943, 329 ,1625 ,1419 ,3282, 3393, 1883,  850, 3491, 3402,   9,  723, 1153 , 672, 1049, 2885, 1336, 1126, 1453, 3020, 1415, 3221, 2680 ,2053, 2511,  851, 1226 ,2008, 1673, 1405 ,2786, 1857 ,1632]
    nodeindex300_100_300 = [2972 , 407, 2910, 2439, 1758, 2965, 2778, 1260, 2417, 2994, 1440, 3583, 1690, 1322, 2705,  954, 2624 , 546 ,1831, 1256, 1765,  104, 2046, 2250, 2445, 3185, 2742, 3216, 1860, 1787, 1378,  738, 2555, 1973 ,1280, 1648 ,2007 ,1025 ,1510 ,1388, 1990 ,2035  ,  7 ,3016, 3062 ,3052, 3512, 2012, 1563, 3460 ,2263,  557  ,939, 1341 ,  79, 1374 , 676, 3239 ,3599, 1609 , 162, 2486 , 734 ,3347, 2481, 2810,  950,  201, 2019, 2076, 3434,  912, 1044,  524, 3407, 1241, 2494 ,1949, 1400,  465 ,1775,  537, 1350,   92 , 905, 1555, 2199,  673,  282, 1193,  216, 2679, 1797, 1704, 1828, 2227, 2156,  593,  236, 2962]
    nodeindex500_100_3000 = [2256 ,1734, 3331 ,1252, 2832, 2523 , 862,  217, 1704 , 487,  165 ,1735, 1332, 1680, 2066,  773, 3137, 2961, 1337, 2506, 2696 ,1687,  803, 1280, 1006, 2288, 3448,  546,  802 ,3074 , 999, 3143 , 349 ,2862, 2020, 1273, 1082, 1309 , 905, 3447, 2314,  117, 3605, 1076 ,2234, 1597 ,2071 , 350, 1198,  535 ,3378 ,2391,  331,  172 , 362, 3052 , 335, 3123 ,2966 , 630 ,2022 , 844 ,2191 ,2309, 2532, 3415, 2024 ,3186  ,305 ,2011,  230 , 978, 2520,  839, 2179,   87 ,2478, 2236, 3272 , 904 ,1333 ,2737 ,1254 ,1399 ,3026 ,2491 ,3124 , 317 , 668 ,3317  ,992 ,2965  ,234 ,2398 , 195 ,2317, 1915 ,3393 ,2667 ,3489]
    nodeindex500_100_30002 = [2703 ,2893 ,1431 , 609 ,1133, 2530,  260, 2671 ,2898 ,2351, 3361, 1706, 3133 ,3080 ,920 ,1613, 2566, 2728,  462, 2427 ,2029 ,3394 ,1834, 471, 2166, 2334, 1729 ,2043 ,3121, 1170,  473 , 972 ,3423, 2942 , 769 ,3097 ,2481,  913 ,1475 ,1491 ,2626, 1231,  145,  361 , 757 ,2846, 442 ,1225,  173 ,2955, 3624 ,  66 ,2540,  103 , 826 ,3328 ,3544 , 995,2146, 1615,  540 ,3350 , 326 ,1546, 1306, 1406,  745 , 526 ,3018, 73, 2959,  721, 2633 ,2049 ,2396,  982, 2302 ,2112 ,2679, 2788, 1283 ,1617, 2294 ,1765, 2588, 2031, 2859 , 555 ,2141 ,1840, 3335 ,3438 ,1884 ,3167,  778, 2131,  475, 1286 ,1979, 2640]

    nodeindex = sorted(nodeindex)
    nodeindex2 = sorted(nodeindex2)
    nodeindex3 = sorted(nodeindex3)
    nodeindex4 = sorted(nodeindex4)

    #print(nodeindex)
    dirtNode, nodelist = computeNodeDirt(file)

    nodeRe = indexTonode(nodeindex500_100_3000, nodelist)
    print(nodeRe)
    inp = "D:\\Git\\Python-Learning\\wntrdemo\\cs11021.inp"
    drawnode(inp, nodeRe)

    #inpfile = "Net2.inp"
    #drawnode(inpfile)