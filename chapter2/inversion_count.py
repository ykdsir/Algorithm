#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/18 22:40
# @Author  : yukaidi
# @File    : inversion_count.py
# @Contact : yukaidi@dingfudata.com
# @Software: PyCharm
# @license : Copyright(C), Dingfu Data

"""
统计逆序对
"""


class InversionCount(object):
    def count(self,array):
        length = len(array)
        return self.__split(array,0,length-1)


    def __split(self,array,low,high):
        if low >= high:
            return 0
        mid = int(low+high)/2
        left = self.__split(array,low,mid)
        right = self.__split(array,mid+1,high)
        count = self.__merge(array,low,mid,high)
        return left+right+count




    def __merge(self,array,low,mid,high):
        # print(low,mid,high)
        begin1 = low
        begin2 = mid+1
        tmp = []
        count = 0
        while begin1 <= mid and begin2 <= high:
            if array[begin1] < array[begin2]:
                tmp.append(array[begin1])
                begin1 += 1
            else:
                tmp.append(array[begin2])
                begin2 += 1
                count += mid-begin1+1
        # print(begin1,mid,begin2,high)
        if begin1 <= mid:
            tmp.extend(array[begin1:mid+1])
        if begin2 <= high:
            tmp.extend(array[begin2:high+1])
        # print(tmp)
        array[low:high+1] = tmp

        begin1 = low
        begin2 = high



        return count


if __name__ == "__main__":
    inversion_count = InversionCount()
    count = inversion_count.count([2, 4, 1, 3, 5])
    print(count)