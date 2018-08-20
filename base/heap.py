#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/19 14:32
# @Author  : yukaidi
# @File    : heap.py
# @Contact : yukaidi@dingfudata.com
# @Software: PyCharm
# @license : Copyright(C), Dingfu Data


class Heap(object):
    def __init__(self, array):
        self.array = array
        self.length = len(array)
        self.heap_size = len(array)
        self.build()

    def parrent(self, i):
        return int(i / 2)

    def leaf_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * (i + 1)
    """
    维护最大堆
    输入为下标i，默认LEFT[i]和RIGHT[i]为最大堆
    """
    def heapify(self,i):
        pass

    def build(self):
        pass
    def sort(self):
        pass

    def insert(self,val):
        pass
