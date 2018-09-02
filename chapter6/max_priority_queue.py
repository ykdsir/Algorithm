#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 20:25
# @Author  : yukaidi
# @File    : max_priority_queue.py
# @Contact : yukaidi@dingfudata.com
# @Software: PyCharm

from max_heap import MaxHeap
import sys


class MaxPriorityQueue(MaxHeap):

    def heap_max(self):
        return self.array[0]

    def extract_max(self):
        if self.heap_size < 1:
            sys.stderr.write('heap underflow')
            return
        max_res = self.array[0]
        self.array[0] = self.array[self.heap_size-1]
        self.heap_size -= 1
        self.heapify(0)
        return max_res

    def increase_key(self,i,k):
        if k < self.array[i]:
            sys.stderr.write('new key is smaller than current key')
        self.array[i] = k
        while i > 0 and self.array[self.parrent(i)] < self.array[i]:
            self.array[self.parrent(i)],self.array[i] = self.array[i],self.array[self.parrent(i)]
            i = self.parrent(i)


