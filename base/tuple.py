#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : hh

'''
当元组里面的对象只有一个时，记得需要加“，”，如果不加的话，就不是元组的数据类型，是字符串的数据类型。
'''
# tuple1=('Python',)
# tuple2=('Python')
# print('tuple1的数据类型:{0},tuple2的数据类型:{1}'.format(type(tuple1),type(tuple2)))

# tuple1 = ('Python', 'Go', 'Java', ['Selenium','Appium'])
# # 显示一个对象在tuple里面的索引位置
# print('Go的索引位置:',tuple1.index('Go'))
# #显示一个对象在tuple里面的个数
# print('Go的个数:',tuple1.count('Go'))

'''
tuple的对象是不可以变化，但是里面对象的值可以改变。
'''
tuple1 = ('Python', 'Go', 'Java', ['Selenium', 'Appium'])
# 修改tuple第四个对象的值
tuple1[3][0] = 'WebDriver'
print('修改tuple对象的值:', tuple1)

# 尝试修改tuple里面的值
tuple1[0] = 'python'
