#DFS深度优先搜索+递归
#每次DFS加1
#check函数检查是'1'且没有遍历过
#理解题意，只要横纵能到达的就是陆地

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally
# or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3
#

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for __ in range(m)]

        def check(i,j):
            if i >= 0 and j >= 0 and i < m and j < n and visited[i][j] == 0 and grid[i][j] == '1':
                visited[i][j] = 1
                return 1

        def dfs(i,j):
            newx = [1,0,-1,0]
            newy = [0,1,0,-1]
            for k in range(4):
                newi = i + newx[k]
                newj = j + newy[k]
                if check(newi,newj):
                    dfs(newi,newj)

        num = 0
        for x in range(m):
            for y in range(n):
                if check(x,y):
                    dfs(x,y)
                    num += 1
        return num

if __name__ == '__main__':
    s= Solution()
    a = s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
    b = s.numIslands(['0'])
    c = s.numIslands([])
    print(a,b,c)
