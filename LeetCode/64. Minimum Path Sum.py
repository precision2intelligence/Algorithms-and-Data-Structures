# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        if m == 1:
            return sum(grid[0])
        if n == 1:
            return sum([grid[i][0] for i in range(m)])
        mapgrid = [[grid[0][0] for _ in range(n)] for __ in range(m)]
        for i in range(1,n):
            mapgrid[0][i] = mapgrid[0][i-1] + grid[0][i]
        for j in range(1,m):
            mapgrid[j][0] = mapgrid[j-1][0] + grid[j][0]
        for i in range(1,m):
            for j in range(1,n):
                mapgrid[i][j] = min(mapgrid[i-1][j],mapgrid[i][j-1]) + grid[i][j]
        return mapgrid[m-1][n-1]


s = Solution()
a = s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
])
print(a)