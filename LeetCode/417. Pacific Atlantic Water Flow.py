#Time O(m*n) 个人理解，三次遍历，两次分别统计两个大洋的dfs，最后一次选重合区域
#Space O(m*n) 个人理解，四个空间，两个分别存储两个大洋的结果，两个visited记录是否访问到

'''
1. 题意的理解：某个点的水可以流向两个大洋，但是正向出发递归难度大，所以从四个边向内流，找到海拔更高的点向上递归
2. 一定注意，两次不同的dfs，所以两个表来存储结果，两个表来记录visited
'''

'''
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        global m,n
        m,n = len(matrix), len(matrix[0])

        global directions, pa_visited, at_visited, paOcean, atOcean
        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
        pa_visited = [[False] * n for _ in range(m)] # 注意写法
        at_visited = [[False] * n for _ in range(m)]
        paOcean = [[0] * n for _ in range(m)]
        atOcean = [[0] * n for _ in range(m)]

        for i in range(m):
            self.dfs(i, 0, 'pa', matrix)
            self.dfs(i, n-1, 'at', matrix)
        for j in range(n):
            self.dfs(0, j, 'pa', matrix)
            self.dfs(m-1, j, 'at', matrix)

        res = list()
        for i in range(m):
            for j in range(n):
                if paOcean[i][j] == 1 and atOcean[i][j] == 1:
                    res.append([i,j])

        return res

    def dfs(self, x, y, oceanFlag, matrix):
        if oceanFlag == 'pa':
            if pa_visited[x][y] == False:
                paOcean[x][y] = 1
                pa_visited[x][y] = True
            else:
                return
        if oceanFlag == 'at':
            if at_visited[x][y] == False:
                atOcean[x][y] = 1
                at_visited[x][y] = True
            else:
                return
        for dx,dy in directions:
            newx = x + dx
            newy = y + dy
            if newx >= 0 and newy >= 0 and newx < m and newy < n:
                if matrix[x][y] <= matrix[newx][newy]:
                    self.dfs(newx, newy, oceanFlag, matrix)
        return



