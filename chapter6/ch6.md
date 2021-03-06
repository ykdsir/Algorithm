# 堆排序

## 堆
数组，近似于完全二叉树。除了最底层，该树是完全充满的。
默认根节点为A[0]
节点i的父节点 i/2
左子节点 2\*i+1
右子节点 2\*(i+1)

**最大堆**
A[PARRENT[i]] >= A[i]
**最小堆**
A[PARRENT[i]] <= A[i]
使用两个变量记录堆的大小，length代表数组的长度，size代表堆的大小，size$\le$length

## 维护堆的性质
以最大堆为例，对每一个非叶子节点，保证其为该节点子树下的最大值，自底向上更新
假设A[LEFT[i]]和A[RIGHT[i]]已为最大堆，调整A[i]中的值，使其满足最大堆的性质。

## 建堆
对非叶子节点，从树的倒数第二层开始，自底向上维护堆的性质，直到树的根节点。

## 堆排序
初始化：建堆
将根节点与堆中最后的元素替换位置。
堆的元素个数减一,维护堆的性质。
如此循环直到最后保持堆性质的堆中只剩下两个元素。
最后得到的数组即为排序好的数组。

## 优先队列
维护由一组元素构成的集合S的数据结构。每一个元素有相关值，称为**关键字**，最大优先队列支持的操作：
1.(S,x) 插入x
2. MAXIMUM(S) 返回具有最大关键字的元素
3. EXTRACT-MAX(S) 去掉并返回最大关键字的元素
4. INCREASE-KEY(S,x,k) 将元素x的关键字增加到k









