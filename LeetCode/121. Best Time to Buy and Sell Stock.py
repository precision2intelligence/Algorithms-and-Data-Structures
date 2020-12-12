# Time:  O(n)
# Space: O(1)

# 更新动规写法

#本质是找到最大最小值之间的差值，但是双层循环会超时
#保存最小买入时机和当前最大收益，如果大于买入时机则判断是否更新收益，小于则更新最小买入，收益只有超过之前才更新
#输入为空或者长度为1的情况要返回‘0’
#不必最小买入和收益，不必为了减少比较而引入最大卖出，可能会有错误

'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''
# 解法一：贪心？
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        maxProfile = 0
        minPrice= prices[0]
        for i in range(1,len(prices)):
            if prices[i] > minPrice and prices[i] - minPrice > maxProfile:
                maxProfile = prices[i] - minPrice
            elif prices[i] < minPrice:
                minPrice = prices[i]
        return maxProfile

# 解法二：动规
class Solution:
    def maxProfit(self, prices):
        m = len(prices)
        if m < 2:
            return 0
        dp = [0, -prices[0]]
        for i in range(1, m):
            dp[0] = max(dp[0], dp[1] + prices[i])
            # 易错：只能买卖一次，所以这里直接是-prices[i]，不需要前一天不持有股票转移过来，这会造成多次交易
            dp[1] = max(dp[1], -prices[i])
        '''
        未优化空间的动规
        dp = [[0, -prices[0]]] + [[0] * 2 for _ in range(m-1)]
        for i in range(1, m):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            # dp[i-1][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[m-1][0]
        '''

        return dp[0]