# Time: O(n)
# Space: O(n)

# 动态规划，分为第i天是否持有股票
# 买或者卖只有一次手续费
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        m = len(prices)
        if m == 1:
            return 0
        dp = [[0] * 2 for _ in range(m)]
        dp[0] = [0, -prices[0]]
        for i in range(1,m):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[m-1][0]


# Time: O(n)
# Space: O(1)

# dp[0]和dp[1]表示第i天手中不持有或者持有股票的收益
# 不理解为什么可以在新dp[0]上操作

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        m = len(prices)
        if m == 1:
            return 0
        dp = [0, 0]
        dp[0] = 0
        dp[1] = -prices[0]
        for i in range(1, m):
            dp[0] = max(dp[0], dp[1]+prices[i]-fee)
            # dp[0]已经更新了，为什么可以直接用
            dp[1] = max(dp[1], dp[0]-prices[i])
        return dp[0]

