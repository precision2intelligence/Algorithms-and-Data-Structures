'''
问题：
使用数组arr中的值代表一种面值的货币，每种面值的货币可以使用任意张，组成aim值，
求使用货币素的最小张数

题解:
dp[i][j]的含义，在可以任意使用arr[0...i]货币的情况下，组成j所需的最小张数
假设计算到位置(i,j),dp[i][j]的值可能来自下面的情况
1.完全不使用当前货币arr[i]的情况下的最少张数,即dp[i-1][j]
2.使用1张货币arr[i]的情况下的最少张数,即dp[i-1][j-arr[i]]+1
3.使用2张货币arr[i]的情况下的最少张数,即dp[i-1][j-2*arr[i]]+2
4.使用3张货币arr[i]的情况下的最少张数,即dp[i-1][j-3*arr[i]]+3
dp[i][j] = min(dp[i-1][j], dp[i][j-arr[i]]+1)
位置i,j依赖位置(i-1,j)，即往上跳一下的位置，也依赖位置(i,j-arr[i])，即往左跳一下的位置
'''

#Time O(N*aim)
#Space O(N*aim)

#初始化表格的时候，aim的列数要+1，否则加不到aim
import sys
def minCoin(arr,aim):
    if not arr or aim < 0:
        return
    row = len(arr)
    dp = [[sys.maxsize] * (aim + 1) for _ in range(row)]
    for j in range(aim+1):
        if j % arr[0] == 0:
            dp[0][j] = j // arr[0]
    for i in range(row):
        dp[i][0] = 0
    for i in range(1,row):
        for j in range(1,aim+1):
            left = sys.maxsize #注意处理面额大于余额的情况
            if j - arr[i] >= 0:
                left = dp[i][j-arr[i]]+1
            dp[i][j] = min(dp[i-1][j],left)
    return dp[row-1][aim]

a = minCoin([1,12,5],11)
print(a)