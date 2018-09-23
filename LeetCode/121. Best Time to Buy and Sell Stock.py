# Time:  O(n)
# Space: O(1)

#本质是找到最大最小值之间的差值，但是双层循环会超时
#保存最小买入时机和当前最大收益，如果大于买入时机则判断是否更新收益，小于则更新最小买入，收益只有超过之前才更新
#输入为空或者长度为1的情况要返回‘0’
#不必最小买入和收益，不必为了减少比较而引入最大卖出，可能会有错误

'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''
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