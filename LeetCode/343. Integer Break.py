#规律题，拆成3比较好，没有3再拆4，也是2*2，观察规律的题

# Given a positive integer n, break it into the sum of
# at least two positive integers and maximize the product
# of those integers. Return the maximum product you can get.
#
# For example, given n = 2, return 1 (2 = 1 + 1); given n = 10,
# return 36 (10 = 3 + 3 + 4).
#
# Note: you may assume that n is not less than 2.
#
# Hint:
#
# There is a simple O(n) solution to this problem.
# You may check the breaking results of n ranging from 7 to 10
# to discover the regularities.

class Solution:#4是一个特殊的数字
    def integerBreak(self, n):  # 数学方法
        if n < 4: return n - 1
        if n == 4: return 4
        q = 0
        while n > 4:
            n -= 3
            q += 1
        return pow(3,q)*n
    def integerBreak(self, n):#本质是查找表
        if n < 4: return n-1
        dp = [0]*(n+1)
        dp[1],dp[2],dp[3] = 1,2,3 #前三个dp不是返回值
        for i in range(4,n+1):
            dp[i] = max(3*dp[i-3],2*dp[i-2])#先拆3，最后可能是0,1,2的余数，即3,4,5.
            # 这里要安排好4=2*2，3=1*3,5=2*3=3*2
        return dp[n]


if __name__ == '__main__':
    solu = Solution()
    print(solu.integerBreak(10))