# 快速排序

## 思想
将数组A[i,j]划分为两个子数组A[i,p-1]和A[p+1,j]，其中A[i,p-1]中的元素均小于A[p]，A[p+1,j]中元素均大于A[p]，然后对子数组排序

```python
def QUICKSORT(A,s,e):
    idx = PARTION(A,s,e)
    QUICKSORT(A,s,idx-1)
    QUICKSORT(A,idx+1,e)
```

确定切分点：使用两个下标记录子数组边界位置，A[p:i]$\le$A[r]；A[i+1:j]>A[r]，

```python
def partion(array,p,r):
    x = array[r]
    i = p-1
    for j in range(p,r):
        if array[j] <= x:
            i += 1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[r] = x,array[i+1]
    return i+1
```




