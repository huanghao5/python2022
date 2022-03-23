#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : hh
list1 = ['Python', 'Allure', 'Pytest']
list2 = ['Java', 'TestNG', 'Allure']
print('获取两个对象里面的共同值:', set(list1) & set(list2))
print('获取两个对象里面的差集:', set(list1) | set(list2))
print('获取两个集合对象里面的包含关系:', set(list1) ^ set(list2))
