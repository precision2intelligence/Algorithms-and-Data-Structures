# Time: O(n) 遍历数组一次
# Space: O(1)

# 常数空间动态规划:用dp保存临时结果

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp, sum = 0, 0
        if len(A) < 3:
            return 0
        for i in range(1, len(A)-1):
            if A[i] - A[i-1] == A[i+1] - A[i]:
                dp += 1
                sum += dp
            else:
                dp = 0
        return sum
