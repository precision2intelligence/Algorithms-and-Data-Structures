# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

#这里和编辑距离一样，是定义一个空表格计算距离，所以一定要初始化list为0
#定义的dp[i]是第i个字符的步数，而不是i-1,边界要清楚
#虽然是动规，考虑最后一步，要从前面写
#开始的时候特例要存储，然后要么return，要么if...elif...else，不然if...else...总会进入else，那是主要动规，特例不应该进入
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n + 1)
        for i in range(n + 1):
            if i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 2
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))