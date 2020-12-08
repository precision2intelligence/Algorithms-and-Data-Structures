# Time:O(n)
# Space:O(n)

## 动规，最难的是冷冻期的理解，是当天结束后开始都是冷冻期，所以状态转移方程要写对

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if not n:
            return 0
        dp = [[0] * 3 for _ in range(len(prices))]
        dp[0] = [-prices[0], 0, 0]
        for i in range(1,n):
            # f[i][0]: 手上持有股票的最大收益
            # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
            # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[n-1][1], dp[n-1][2])
