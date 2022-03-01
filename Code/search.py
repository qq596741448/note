from cal_time import *

@cal_time
def linear_search(li, val):
    for ind, tar in enumerate(li):
        if val == tar:
            return ind
    else:
        return False


@cal_time
def binary_search(li,val):
    left = 0
    right = len(li)-1
    while left <= right:
        mid = (left+right)//2
        if val == li[mid]:
            return mid
        elif val < li[mid]:
            right = mid -1
        else:
            left = mid +1
    else:
        return None

li=list(range(1000000))
linear_search(li,389000)
binary_search(li,389000)