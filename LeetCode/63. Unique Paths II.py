#一个重要的错误：即使在左边和上边，如果有障碍，障碍后面的全是0，不能设为1，是永远到不了的。否则出错。

# Time:  O(m * n)
# Space: O(m * n)
#
# Follow up for "Unique Paths":
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
#
# Note: m and n will be at most 100.
#
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for __ in range(n)] for __ in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j] == 0 else 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]