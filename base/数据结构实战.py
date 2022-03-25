#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : hh

'''
字符串列列表相互转换
'''


def str_list():
    str1 = "hello word"
    # 把字符串的数据类型转为列表的数据类型
    str_list = str1.split(" ")
    print(str_list)
    print(type(str_list))
    # 把列表的数据类型转为字符串
    list_str = " ".join(str_list)
    print(list_str)
    print(type(list_str))


if __name__ == '__main__':
    str_list()
