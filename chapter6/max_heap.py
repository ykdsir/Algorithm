#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/19 14:47
# @Author  : yukaidi
# @File    : max_heap.py
# @Contact : yukaidi@dingfudata.com
# @Software: PyCharm
# @license : Copyright(C), Dingfu Data

from base.heap import Heap


class MaxHeap(Heap):
    def heapify(self, i):
        while i < self.heap_size:
            # print(i)
            l = self.leaf_child(i)
            r = self.right_child(i)
            if l < self.heap_size and self.array[i] < self.array[l]:
                largest = l
            else:
                largest = i
            if r < self.heap_size and self.array[largest] < self.array[r]:
                largest = r
            # print(largest)
            if largest != i:
                self.array[i], self.array[largest] = self.array[largest], self.array[i]
                i = largest
            else:
                break

    def build(self):
        self.heap_size = self.length
        leaf_begin = int(self.heap_size / 2)
        for x in range(leaf_begin - 1, -1, -1):
            self.heapify(x)
            # print(self.array)

    def sort(self):
        # 默认已经做好了堆的初始化
        for x in range(self.length-1,0,-1):
            self.array[0],self.array[x] = self.array[x],self.array[0]
            self.heap_size -= 1
            self.heapify(0)


if __name__ == "__main__":
    max_heap = MaxHeap([1, 23, 4, 45, 56, 587])
    print(max_heap.array)
    max_heap.sort()
    print(max_heap.array)
    max_heap.build()
    print(max_heap.array)
