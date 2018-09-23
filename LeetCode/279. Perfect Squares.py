#动态规划，Python比Python3要快

# Time:  O(n * sqrt(n))
# Space: O(n)
#
# Given a positive integer n, find the least number of perfect
# square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4;
# given n = 13, return 2 because 13 = 4 + 9.
#

#解法一：
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        output = [0x7fffffff] * (n + 1)
        output[0] = 0
        output[1] = 1
        for i in range(2, n + 1):
            j = 1
            while (j * j <= i):
                output[i] = min(output[i], output[i - j * j] + 1)
                j = j + 1

        return output[n]

#解法二：
class Solution(object):
    def numSquares(self, n):
        dp = [x for x in range(n+1)] #四平方和定理，dp[k]<=4
        for i in range(1,n+1):
            for j in range(1,int(i**(0.5))+1):
                dp[i]=min(dp[i],dp[i-j*j]+1)
        return dp[n]

