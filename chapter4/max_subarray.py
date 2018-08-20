#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/19 10:33
# @Author  : yukaidi
# @File    : max_subarray.py
# @Contact : yukaidi@dingfudata.com
# @Software: PyCharm
# @license : Copyright(C), Dingfu Data

import sys
import numpy as np
import time


class MaxSubArray(object):
    def voilent_search(self, array):
        begin_time = time.time()
        length = len(array)
        max_sum = 0
        low = 0
        high = 0
        for i in range(0, length - 1):
            for j in range(i + 1, length):
                tmp_sum = sum(array[i:j + 1])
                if tmp_sum > max_sum:
                    max_sum = tmp_sum
                    low = i
                    high = j
        end_time = time.time()
        print('violent total time: %s'%(str(end_time - begin_time)))
        return max_sum, low, high

    def split_search(self,array):
        begin_time = time.time()
        res = self.__split_search(array,0,len(array)-1)
        end_time = time.time()
        print('split total time: %s'%(str(end_time - begin_time)))
        return res

    def __split_search(self,array,low,high):
        if low ==high:
            return array[low],low,high
        mid = (low+high)/2
        left_sum,left_begin,left_end = self.__split_search(array,low,mid)
        right_sum,right_begin,right_end = self.__split_search(array,low+1,high)
        cross_sum,cross_begin,cross_end = self.__cross_max(array,low,mid,high)

        max_sum = 0
        begin_idx = 0
        end_idx=  0

        if left_sum>right_sum:
            max_sum,begin_idx,end_idx = left_sum,left_begin,left_end
        else:
            max_sum,begin_idx,end_idx = right_sum,right_begin,right_end

        if max_sum > cross_sum:
            return max_sum,begin_idx,end_idx
        else:
            return cross_sum,cross_begin,cross_end


    def __cross_max(self,array,low,mid,high):
        # print(low,mid,high)
        left_sum = -sys.maxint
        sum = 0
        left_idx = 0
        right_idx = 0
        for x in range(mid,low-1,-1):
            sum += array[x]
            if sum > left_sum:
                left_sum = sum
                left_idx = x
        right_sum = -sys.maxint
        sum = 0
        for y in range(mid+1,high+1):
            sum += array[y]
            if sum > right_sum:
                right_sum = sum
                right_idx = y
        return left_sum+right_sum,left_idx,right_idx

    # def linear_search(self,array):
    #     length = len(array)
    #     max_sum = -sys.maxint
    #     tmp_sum = array[0]
    #     low = 0
    #     high = 0
    #     for x in range(1,length):
    #         if tmp_sum == 0:
    #             low = x
    #         tmp_sum += array[x]
    #         if tmp_sum> max_sum:
    #             max_sum = tmp_sum
    #             high = x
    #         elif tmp_sum < 0:
    #             tmp_sum = 0
    #
    #     return max_sum,low,high
    def dynamic_search(self,array):
        begin_time = time.time()
        length = len(array)
        max_sum = 0
        low = 0
        high = 0
        sum = 0
        for x in range(0,length):
            if sum >= 0:
                sum += array[x]
            else:
                sum = array[x]
                low = x
            if sum > max_sum:
                max_sum = sum
                high = x
        end_time = time.time()
        print('dynamic total time: %s'%(str(end_time-begin_time)))
        return max_sum,low,high



if __name__ == "__main__":
    max_subarray = MaxSubArray()
    for x in range(1):
        array = np.random.randint(-10000,10000,100)
        # print(array)
        print(max_subarray.voilent_search(array))
        # print(max_subarray.split_search(array))
        print(max_subarray.dynamic_search(array))