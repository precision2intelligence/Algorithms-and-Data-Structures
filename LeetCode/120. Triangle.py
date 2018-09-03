#空间复杂度还可以更低
#特例是没行第0个和最后一个
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [[0] * (i+1) for i in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1,n):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
        return min(dp[n-1][:])

s = Solution()
a = s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])
print(a)