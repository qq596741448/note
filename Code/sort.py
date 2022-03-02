import  random
from cal_time import *
import copy
import sys
import heapq
sys.setrecursionlimit(100000)


# 冒泡排序
@cal_time
def bubb_sort(li):
    for i in range(len(li)-1): #第i趟
        exchange = False
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if exchange == False:
            return

#选择排序
@cal_time
def select_sort(li):
    for i in range(len(li)-1):
        min_val = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_val] :
                min_val = j
        li[i], li[min_val] = li[min_val], li[i]

#插入排序
@cal_time
def insert_sort(li):
    for i in range(1,len(li)):  # 摸到的牌
        temp = li[i]
        j = i - 1   #手里的牌
        while li[j]>temp and j>=0:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = temp

#快速排序
@cal_time
def quick_sort(li):
    _quick_sort(li,0,len(li)-1)

def _quick_sort(li,left,right):
    if left<right:
        mid = partition(li,left,right)
        _quick_sort(li,left,mid-1)
        _quick_sort(li,mid+1,right)

def partition(li,left,right):
    temp = li[left]
    while left<right:
        while left<right and li[right]>=temp:  #右边大于选的数，right--
            right -= 1
        li[left] = li[right] #退出说明找到比temp小的数，交换
        while left<right and li[left]<=temp :
            left += 1
        li[right] = li[left]
    li[left] = temp
    return left

# 堆排序
"""
range(start, stop[, step])
参数说明：
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
"""

def sift(li,low,high):  # low堆顶     high最后一个
    i = low
    j = 2 * i +1
    temp = li[low]
    while j <= high:
        if j+1<=high and li[j+1] > li[j]: #两边都有且哪个大
            j = j + 1
        if li[j]>temp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = temp
            break
    else:
        li[i] = temp    # 把temp放在叶子节点

def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2,-1,-1):
        sift(li,i,n-1) #建堆完成
    for i in range(n-1,-1,-1): # 当前堆的最后一个元素
        li[0],li[i] = li[i],li[0]
        sift(li,0,i-1)

def merge(li,low,mid,high):
    i = low
    j = mid + 1
    ltmp = []
    while i<=mid and j<=high:
        if li[i]<li[j]:
            ltmp.append(li[i])
            i +=1
        else:
            ltmp.append(li[j])
            j +=1
    # 执行完，有一部分没数，另一部分剩下，判断在哪边，全部填上
    while i<=mid:
        ltmp.append(li[i])
        i += 1
    while j<=high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp

def merge_sort(li,low,high):
    if low<high:
        mid = (low+high)//2
        merge_sort(li, low, mid)    # 左边
        merge_sort(li,mid+1,high)   # 右边
        merge(li,low,mid,high)      # 归并

def insert_sort_gap(li,gap):
    for i in range(gap,len(li)):   #重点是gap的位置
        temp = li[i]
        j = i - gap
        while li[j]>temp and j>=0:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = temp

def shell_sort(li):
    d = len(li)//2            #长度的一半为d
    while d>=1:
        insert_sort_gap(li,d)
        d //= 2

def count_sort(li,max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind,val in enumerate(count):
        for i in range(val):
            li.append(ind)

def bucket_sort(li,n=100,max_num=1000000):    #一百个桶，最大数10000
    buckets = [[] for _ in range(n)]    #创建桶
    for var in li:
        i = min(var // (max_num//n),n-1)          #var放在几号桶
        buckets[i].append(var)
        #保持桶内顺序
        for j in range(len(buckets[i])-1,0,-1):
            if buckets[i][j] <buckets[i][j-1]:
                buckets[i][j],buckets[i][j-1] = buckets[i][j-1],buckets[i][j]
            else:
                break
    new_li = []
    for buc in buckets:
        new_li.extend(buc)
    return new_li

def radix_sort(li):
    max_num = max(li)   #最大值 99 -> 做2次   888 -> 做3次
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for var in li:
            # 987 it=1 取7
            dig = (var // 10 ** it) % 10
            buckets[dig].append(var)
        li.clear()
        for buc in buckets:
            li.extend(buc)
        it += 1



li = [random.randint(0,1000) for _ in range(100)]
radix_sort(li)
print(li)

