#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/1 11:39
# @Author  : yukaidi
# @File    : counting_sort.py
# @Contact : yukaidi@dingfudata.com
# @Software: PyCharm

from base.sort import Sort
import numpy as np


class CountingSort(Sort):
    def sort(self,array, maxsize):
        C = [0] * maxsize
        length = len(array)
        result = [0] * length
        for x in range(length):
            C[array[x]] += 1

        for x in range(1,maxsize):
            C[x] = C[x] + C[x-1]

        for idx in range(length-1,-1,-1):
            # print(idx)
            # print(array[idx])
            # print(C[array[idx]])
            # print('*'*20)
            result[C[array[idx]]-1] = array[idx]
            C[array[idx]] -= 1
        return result

    def test(self, array=[123, 1321, 343, 52, 35, 454, 7, 57, 4234, 2, 323]):
        max_size = 200
        array = np.random.randint(0, max_size, 20)
        print('before sort: ',array)
        print('after sort',self.sort(array,max_size))


if __name__ == '__main__':
    count_sort = CountingSort()

    count_sort.test()

