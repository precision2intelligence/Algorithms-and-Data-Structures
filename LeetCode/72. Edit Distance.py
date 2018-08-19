# Time:  O(n * m)
# Space: O(n * m)
# Method: DP

#Note:
#初始化表格的时候用列表生成式，因为复制会导致一个位置变动对应位置全部变动。
#word1作为行，word2作为列。顺序颠倒容易索引出错。


class Solution:

    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        #填表
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    delete = dp[i-1][j] + 1
                    insert = dp[i][j-1] + 1
                    replace = dp[i-1][j-1] +1
                    dp[i][j] = min(delete,insert,replace)

        return dp[m][n]

if __name__ == "__main__":
    s = Solution()
    res = s.minDistance('word','wwoold')
    print(res)
