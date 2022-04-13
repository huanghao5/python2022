#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : hh

def func(name):
    print("name {0}".format(name))


def func1(age=18):
    print("age {0}".format(age))


def func2(*args, **kwargs):

    print("*args {0}, **kwargs {1}".format(args,kwargs))
    print(type(args))



if __name__ == '__main__':
    func(name="张三")

    func1(age=19)

    func2((1,2),name="lisi")