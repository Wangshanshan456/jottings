# -*- coding: utf-8 -*-
"""
 @Time    : 2018/11/3 0003 上午 9:21
 @Author  : Shanshan Wang
 @Version : Python3.5
 @Function:pandas简介以及数据结构series详解
"""
import pandas as pd
import numpy as np





# 熊猫( panda的名词复数 )
# pandas 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。
# Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。
# pandas提供了大量能使我们快速便捷地处理数据的函数和方法。
# 你很快就会发现，它是使Python成为强大而高效的数据分析环境的重要因素之一。

# pandas 依赖python库：setuptools numpy python-dateutil  pytz
# pandas 的三大作用：数据的引入 数据的特征提取  数据的清洗

# pandas的基本数据结构：Series和DataFrame
# Series：一种类似于一维数组的对象，是由一组数据（各种numpy数据类型）以及一组与之相关的
# 数据标签（即索引）组成。仅由一组数据也可产生简单的Series对象，注意：Series中的索引值是可以重复的

# DataFrame数据框架：一个表格型的数据结构，包含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型等）
# DataFrame既有行索引也有列索引，可以被看作是由Series组成的字典

# 第一种：Series通过一维数组创建

# 通过数组创建Series的时候，如果没有为数据指定索引的话，会自动创建一个从0到n-1的整数索引
# 当Series对象创建好后，可以通过index修改索引值
# 明确给定索引值与数据类型

# 第二种：Series通过字典的方式创建
arr=np.random.randint(10,20,(3,4))
print(arr)
arr=np.array([22,33,np.nan,90])
#[22. 33. nan 90.] float64
print(arr,arr.dtype)
s1=pd.Series(arr)
# 0    22.0
# 1    33.0
# 2     NaN
# 3    90.0
# dtype: float64
print(s1)
#float64
print(s1.dtype)
#RangeIndex(start=0, stop=4, step=1)
print(s1.index)
#[22. 33. nan 90.]
print(s1.values)
#注意：索引值可以重复
s1.index=[u'东方','a1','a2','a1']
# 东方    22.0
# a1    33.0
# a2     NaN
# a1    90.0
# dtype: float64
print(s1)

s2=pd.Series(data=[88,99,100],index=['语文','数学','外语'],dtype=np.float)
# 语文     88.0
# 数学     99.0
# 外语    100.0
# dtype: float64
print(s2)
#通过字典创建
dict1={'语文': 88, '数学': 99, '外语': 100}
s3=pd.Series(dict1,dtype=np.float)
# 外语    100.0
# 数学     99.0
# 语文     88.0
# dtype: float64
print(s3)

# Series值的获取的两种方式：
# 1、通过方括号+索引的方式获取对应索引的数据，可能返回多条数据
# 2、通过方括号+下标值的方式获取数据，下标值的取值范围为：[0, len(Series.values))；另外下标值也可以是负数，表示从右往左获取数据

# Series获取多个值的方式类似Numpy中的ndarray的切片操作
# 通过方括号+下标值/索引值+冒号(的形式来截取series对象中的一部分数据
print('**************************************')
dict1={'语文': 88, '数学': 99, '外语': 100}
s1=pd.Series(dict1,dtype=np.float)
print(s1)
# 数学    99.0
# 语文    88.0
# dtype: float64
#注意：使用下标值切片是前闭后开区间，使用索引值去切片是全闭区间
print(s1['数学':'语文'])
# 数学    99.0
# dtype: float64
print(s1[1:2])
arr1=np.array([100,20,30])
# 外语    200.0
# 数学    119.0
# 语文    118.0
# dtype: float64
print(s1+arr1)

s2=pd.Series({'dfy': 100, 'zhangsan': 88})
s2.index=['a','b']
print(s2)
s2=pd.Series(s2,index=['dfy', 'zhangsan', 'c'])
# dfy        NaN
# zhangsan   NaN
# c          NaN
# dtype: float64
print(s2)
s2[pd.isnull(s2)]=0
# dfy         0.0
# zhangsan    0.0
# c           0.0
# dtype: float64
print(s2)

#自动对齐
s4=pd.Series(data=[22,33,44],index=['s1','s2','s3'])
s5=pd.Series(data=[22,33,44],index=['s3','s4','s2'])
# s1     NaN
# s2    77.0
# s3    66.0
# s4     NaN
# dtype: float64
#对应索引的位置会相加
print(s4+s5)

# name series对象  index也有name属性
s6=pd.Series({'dfy': 100, 'zs': 88, 'ls': 99})
s6.name='数学'
s6.index.name='考试成绩'
# 考试成绩
# dfy    100
# ls      99
# zs      88
# Name: 数学, dtype: int64
print(s6)

# 注意：使用下标值去切片是前闭后开区间 使用索引值去切片是全闭区间

# Series的运算
# numpy中的数组运算，在Series中都保留了，都可以使用，并且Series在进行数组运算的时候
# 索引与值之间的映射关系不会发生改变
# 注意：其实在操作Series的时候，基本上可以把Series看成numpy中的一维数组来进行

# NaN在pandas中表示一个缺失值或NA值
# pandas中的isnull和notnull两个函数可以用于在Series中检测缺失值，这两个函数返回一个布尔类型的Series
# 可以快速找到缺失值并给其赋一个默认值

# Series自动对齐
# 当多个series对象之间进行运算的时候，如果不同series之间具有不同的索引值，那么运算会
# 自动对齐不同索引值的数据，如果某个series没有某个索引值，那么结果会赋值为NaN

# Series及其索引的name属性
# Series对象本身与其索引都有一个name属性，默认为空，根据需要可以进行赋值操作
