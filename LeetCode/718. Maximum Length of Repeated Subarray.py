#同Road to Python的解法

# Time:  O(m * n)
# Space: O(m + n)

# Given two integer arrays A and B,
# return the maximum length of an subarray that appears in both arrays.
#
# Example 1:
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation:
# The repeated subarray with maximum length is [3, 2, 1].
# Note:
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100

class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        lstr1 = len(A)
        lstr2 = len(B)
        record = [[0 for i in range(lstr2+1)] for j in range(lstr1+1)]  # 多一位
        maxNum = 0          # 最长匹配长度
        p = 0               # 匹配的起始位

        for i in range(lstr1):
            for j in range(lstr2):
                if A[i] == B[j]:
                    # 相同则累加
                    record[i+1][j+1] = record[i][j] + 1
                    if record[i+1][j+1] > maxNum:
                        # 获取最大匹配长度
                        maxNum = record[i+1][j+1]
                        # 记录最大匹配长度的终止位置
                        p = i + 1
        return maxNum