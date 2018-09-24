# Time:  O(n)
# Space: O(n)

#两次操作，就是分成前i天的收益和i之后的收益
#如果直接每次都按i计算，则超时，故考虑计算一次存入表里
#first从左往右，second从右往左，注意second的边界
#最后巧用max函数，求出最大，省去if……else……

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l<=1: return 0
        first,second = [0 for i in range(l)],[0 for i in range(l+1)]
        minp = prices[0]
        for i in range(1,l):
            first[i] = max(prices[i] - minp, first[i-1])
            if prices[i] < minp:
                minp = prices[i]
        maxp = prices[l-1]
        for j in range(l-1,-1,-1):
            if prices[j] > maxp:
                maxp = prices[j]
            second[j] = max(maxp - prices[j-1],second[j+1])
        ans = 0
        for i in range(l):
            ans = max(ans,first[i] + second[i+1])
        return ans