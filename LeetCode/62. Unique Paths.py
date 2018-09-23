# Time:  O(m * n)
# Space: O(m * n)
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
# Note: m and n will be at most 100.
#

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        martix = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if j == 0 or i == 0:
                    martix[i][j] = 1
                else:
                    martix[i][j] = martix[i - 1][j] + martix[i][j - 1]
        return martix[m - 1][n - 1]
