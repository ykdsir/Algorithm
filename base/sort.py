#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/18 18:07
# @Author  : yukaidi
# @File    : sort.py
# @Contact : yukaidi@dingfudata.com
# @Software: PyCharm
# @license : Copyright(C), Dingfu Data

import sys


class Sort(object):
    def sort(self, array):
        if isinstance(array,list):
            sys.stderr.write(str(list) + 'is not type list')
        pass

    def test(self, array=[123, 1321, 343, 52, 35, 454, 7, 57, 4234, 2, 323]):
        pass

    def check_order(self,array):
        length = len(array)
        for x in range(1,length):
            if array[x] < array[x-1]:
                return False
        return True