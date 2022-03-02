class Solution(object):
    def searchMatrix(self, matrix, target):
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