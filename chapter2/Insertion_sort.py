#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/18 18:06
# @Author  : yukaidi
# @File    : Insertion_sort.py.py
# @Contact : yukaidi@dingfudata.com
# @Software: PyCharm
# @license : Copyright(C), Dingfu Data

from base.sort import Sort
import numpy as np


class InsertionSort(Sort):
    def sort(self, array):
        length = len(array)
        for x in range(1, length):
            tmp = array[x]
            while(x > 0) and array[x - 1] > tmp:
                array[x] = array[x - 1]
                x = x - 1
            array[x] = tmp
            # print(array)
        return array

    def test(self, array=[123, 1321, 343, 52, 35, 454, 7, 57, 4234, 2, 323]):
        array = np.random.randint(0, 10000, 100)
        array = self.sort(array)
        print(array)
        return array


if __name__ == "__main__":
    insertion_sort = InsertionSort()
    array = insertion_sort.test()
    print(insertion_sort.check_order(array))
