#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/18 20:12
# @Author  : yukaidi
# @File    : merge_sort.py
# @Contact : yukaidi@dingfudata.com
# @Software: PyCharm
# @license : Copyright(C), Dingfu Data

from base.sort import Sort
import numpy as np


class MergeSort(Sort):
    def sort(self, array):
        length = len(array)
        self.__split(array,0,length - 1)
        return array

    def __split(self,array,low,high):
        if(low >= high):
            return
        mid = int((low+high)/2)
        self.__split(array,low,mid)
        self.__split(array,mid+1,high)
        self.__merge(array,low,mid,high)

    def __merge(self,array,low,mid,high):
        # print(low,mid,high)
        begin1 = low
        begin2 = mid+1
        tmp = []
        while begin1 <= mid and begin2 <= high:
            if array[begin1] < array[begin2]:
                tmp.append(array[begin1])
                begin1 += 1
            else:
                tmp.append(array[begin2])
                begin2 += 1
        # print(begin1,mid,begin2,high)
        if begin1 <= mid:
            tmp.extend(array[begin1:mid+1])
        if begin2 <= high:
            tmp.extend(array[begin2:high+1])
        # print(tmp)
        array[low:high+1] = tmp
        # print(array)



    def test(self, array=[123, 1321, 343, 52, 35, 454, 7, 57, 4234, 2, 323]):
        array = np.random.randint(0,1000,100)
        print(self.sort(array))
        return array


if __name__ == "__main__":
    merge_sort = MergeSort()
    array = merge_sort.test()
    print(merge_sort.check_order(array))
