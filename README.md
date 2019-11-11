# SensorPlacementInDistributionNetworks

## 供水管网水质监测点/传感器布局优化

### 1.基于整数编码的NSGA2算法
### 2.最短监测时间与最大监测概率双目标函数
### 3.使用基于epanet的wntr库进行水力水质模拟,并处理结果
### 4.将处理结果代入NSGA2算法, 迭代计算出结果
### 5. 所有功能基本实现, 流程基本可以走通



## 程序概述
本程序主要是解决供水管网水质监测点的布局优化问题；

面向的是突发污染情况下的水质监测点选取，因此需要多节点进行水质污染注入实验；

之前的做法都是使用epanet的程序包，链接库，但USEPA之后开源了基于Python的水力水质模拟库WNTR；

因此本程序使用了WNTR进行水力水质模拟，编写了水质模拟、数据处理模块；用于解决污染实验的实现与数据收集处理；

由于选择监测点是布局优化问题，因此使用了常见的进化算法NSGA2——非支配遗传算法；

水质监测布局常用的目标是最小化监测时间和最大化监测事件，即一组监测点尽可能对污染事件发生响应最快，对污染事件监测到的数量最多即为最优，但两个目标属于负相关。

有关帕累托解、NGSA2算法请自行搜索其他资料。

本程序实现了水质模拟、数据处理、算法迭代的全部过程。



## 基本使用
详情参见example文件夹的`example1.py`和`example2.py`   
分别是基于无文件和读取文件的形式来走完整个流程



##  程序框架

主要文件功能如下，部分未列出

```
-> example
	-> example1.py		# 无文件示例
	-> example2.py		# 读取文件示例

-> function
	-> funModel.py	# 目标函数抽象类
	-> funUserDefine.py	# 目标函数子类
	
-> nsga2
	-> crossover.py	# 交叉
	-> crowddist.py	# 拥挤度计算
	-> dominance.py	# 支配计算
	-> dominanceMain.py	# 支配主程序
	-> estimate.py	# 
	-> finalMain.py	# 算法主函数
	-> mutation.py	# 变异
	-> population.py # 种群生成
	-> rank.py	# 排序
	-> selection.py	# 选择
	-> WeightMain.py	# 权重计算

-> simulation
	-> WaterQualitySim.py	# 水质模拟
	-> WaterQualitySimData.py	# 结果数据处理
	-> IndexToNode.py	# 转换回原有节点名称

-> final.py # 自用函数
```

