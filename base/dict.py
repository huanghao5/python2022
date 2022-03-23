#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : hh

# dict1 = {'name': 'admin', 'age': 18, 'address': 'beijing', 'work': 'python'}
# # 获取字典里面所有的key值
# for item in dict1.keys():
#     print(item)
# # 获取字典里面所有的value的值 for item in dict1.values():
# print(item)
# # 依据key来修改和获取字典的值
# print('name对应的值内容为:', dict1['name'])
# dict1['name'] = '张三'
# print('修改后的字典内容:', dict1)
# # 字典里面增加新的值内容
# dict1['薪资'] = 30
# print('增加内容后的字典:', dict1)
# # 两个字典的合并
# dict2 = {'company': '阿里巴巴'}
# dict1.update(dict2)
# print('两个字典合并后的内容:', dict1)


# dict1 = {'name': 'admin', 'age': 18, 'address': 'beijing', 'work': 'python'}
# for k, v in dict1.items():
#     print(k, ":", v)


dict1 = {'name': 'admin', 'age': 18, 'address': 'beijing', 'work': 'python'}
key_dict1 = sorted(dict1.items(), key=lambda item: item[0])
print('依据key对象对字典排序后的结果信息:\n', key_dict1)
# 根据valie来对字典进行排序
value_dict1 = sorted(dict1.items(), key=lambda item: item[1])
print('依据value对象对字典排序后的结果信息:\n', value_dict1)
