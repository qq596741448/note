# leetcode

## 一、排序

### [242. 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/)

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false





思路：

次数相同 -> 长度一样

1.字符串排序 

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return s == t
        ss=list(s)
        tt=list(t)
        ss.sort() 
        tt.sort()
        return ss==tt

```

2.字典

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return s == t

        dict1={}
        dict2={}
        for ch in s:
            dict1[ch]= dict1.get(ch,0) +1
        for ch in t:
            dict2[ch]= dict2.get(ch,0) +1       
        return dict1 == dict2     
```



### [74. 搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

```
输入：matrix = [
[1,3,5,7],
[10,11,16,20],
[23,30,34,60]], target = 3
输出：true
```

```
输入：matrix = [
[1,3,5,7],
[10,11,16,20],
[23,30,34,60]], target = 13
输出：false
```

**思路：**使用二分查找

**难点：**

1、怎么把mid变成二维

2、二分查找的代码如何实现

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        h = len(matrix)  # 行数   3
        if h ==0:
            return False
        w = len(matrix[0])  # 列数   4
        if w == 0:
            return False
        left = 0
        right = w * h - 1  # 最后一位11
        while left <= right:
            mid = (left + right) // 2  # mid=5
            i = mid // w  # 确认mid行数
            j = mid % w
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                right = mid -1
            else:
                left = mid +1
        else:
            return False
```



## 二、其他问题

### 1.汉诺塔问题

当n=2时：

<img src="../assets/leetcode_note/image-20220223103639706.png" alt="image-20220223103639706" style="zoom: 50%;" />



当n个盘子时：

<img src="../assets/leetcode_note/image-20220223103801180.png" alt="image-20220223103801180" style="zoom:50%;" />

```python
def hanoi(n, a, b, c):
    if n>0:
        hanoi(n-1, a, c, b)
        print("moving from %s -> %s" % (a,c))
        hanoi(n-1, b, a, c)

hanoi(4,'A','B','C')
```

第一步：n-1个盘子移动到B（经过C）

第二步：第n个盘子移动到C

第三步：n-1个盘子移动到C（经过A）

