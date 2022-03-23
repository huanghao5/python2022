#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : hh

'''
'append',
'insert'
 'clear',
'copy',
'count',
'extend',
'index', '',
'pop',
'remove',
'reverse',
'sort'
'''

# #append:添加的列表是在列表的最后一位
# #新建一个列表
# list1 = [1,2,3]
# #使用append向list1中添加元素
# list1.append(4)
# print(list1)

# # insert:根据自己的需求insert到列表的索引位置
# # 新建一个列表
# list1 = [1, 2, 3]
# # 使用insert添加元素，insert方法会有两个参数insert（位置下标，元素值）
# list1.insert(3, 4)
# print(list1)

list1 = ['Java', 'Go', 'Python', 'PHP']
# count:列表中的对象在列表中存在几位
print('python在列表中存在几位:', list1.count('Python'))
# 寻找出对象的索引信息
print('Python在列表里面的索引信息:', list1.index('Python'))
# pop:默认删除列表里面的最后一位对象并且返回来
print('删除的对象返回来:', list1.pop())
# remove:在列表里面删除指定的元素信息
list1.remove('Python')
print('在列表里面删除Python的对象:', list1)
# 新增一个可interable的对象信息
list1.extend(['selenium', 'appium'])
# clear 列表的清空
list1.clear()
print('清空后的列表内容:{0},列表⻓度:{1}'.format(list1, len(list1)))
