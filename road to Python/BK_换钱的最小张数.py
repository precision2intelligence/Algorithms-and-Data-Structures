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

#经过空间压缩的动态规划
def minCoins2(arr, aim):
    if arr == None or len(arr) == 0 or aim < 0:
        return -1
    row = len(arr)
    dp = [sys.maxsize for i in range(aim+1)]
    dp[0] = 0
    for i in range(1, aim+1):
        if i % arr[0] == 0:
            dp[i] = i // arr[0]
    for i in range(1, row):
        dp[0] = 0
        for j in range(1, aim+1):
            left = sys.maxsize
            if j - arr[i] >= 0 and dp[j-arr[i]] != sys.maxsize:
                left = dp[j-arr[i]] + 1
            dp[j] = min(left, dp[j])
    return dp[aim] if dp[aim] != sys.maxsize else -1
'''
问题2:
问题1的基础上，数组arr中的货币不是无限使用的，用完就没有。
arr = [2, 3, 5]
aim = 20

题解2：
dp[i][j]的含义，在可以任意使用arr[0...i]货币的情况下（每个值权代表一张货币），组成j所需的最小张数
如，dp[0][0...aim]，表示只能使用一张arr[0]货币的情况下，找某个钱数的最小张数。
假设计算到位置(i,j),dp[i][j]的值可能来自下面的情况
1.上边，对于dp[i-1][j]表示，任意使用arr[0...i-1]货币的情况下，组成j所需的最小张数，dp[i][j]可能与其相等
2.左上边，因为arr[i]只有一张不能重复，我们考虑dp[i-1][j-arr[i]],表示在可以任意使用arr[0...i-1]货币的情况下，组成j-arr[i]所需的最小张数。
所以dp[i][j]=dp[i-1][j-arr[i]]+1
注意，本题不能像minCoins2那样使用空间压缩。
因为在dp[j - arr[i]]的使用，可能已经使用了当前的货币i
'''
def minCoins3(arr, aim):
    n = len(arr)
    inf = float('inf')
    dp = [[0] * (aim + 1) for i in range(n)]
    # 第0行的初始化，除了使用货币自身(arr[0])，其他都为inf
    for j in range(1, aim + 1):
        dp[0][j] = inf
    if arr[0] <= aim:
        dp[0][arr[0]] = 1
    for i in range(1, n):
        for j in range(1, aim + 1):
            leftup = dp[i - 1][j - arr[i]] + 1 \
                if j - arr[i] >= 0 and dp[i - 1][j - arr[i]] != inf \
                else inf
            dp[i][j] = min(leftup, dp[i - 1][j])
    return dp[n - 1][aim] if dp[n - 1][aim] != inf else -1


a = minCoins3([1,12,5],11)
print(a)