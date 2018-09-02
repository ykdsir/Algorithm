#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 21:24
# @Author  : yukaidi
# @File    : quick_sort.py
# @Contact : yukaidi@dingfudata.com
# @Software: PyCharm

from base.sort import Sort
import numpy as np

class QuickSort(Sort):
    def sort(self, array):
        self.quicksort2(array,0,len(array)-1)

    def quicksort(self,array,begin,end):
        if end <= begin:
            return
        idx = self.partion(array,begin,end)
        self.quicksort(array,begin,idx-1)
        self.quicksort(array,idx+1,end)

    # 消除尾递归
    def quicksort2(self,array,begin,end):
        while begin < end:
            idx = self.partion(array, begin, end)
            self.quicksort(array, begin, idx - 1)
            begin = idx + 1

    def partion(self,array,p,r):
        x = array[r]
        i = p-1
        for j in range(p,r):
            if array[j] <= x:
                i += 1
                array[i],array[j] = array[j],array[i]
        array[i+1],array[r] = x,array[i+1]
        return i+1

    def random_partion(self,array,p,r):
        i = np.random.randint(p,r)
        array[i],array[r] = array[r],array[i]
        return self.partion(array,p,r)

    def random_quicksort(self,array,begin,end):
        if end <= begin:
            return
        idx = self.random_partion(array,begin,end)
        self.quicksort(array,begin,idx-1)
        self.quicksort(array,idx+1,end)


    def test(self, array=[123, 1321, 343, 52, 35, 454, 7, 57, 4234, 2, 323]):
        array = np.random.randint(-1000,1000,20)
        self.sort(array)
        print(array)

if __name__ == "__main__":
    quickSort = QuickSort()
    quickSort.test()