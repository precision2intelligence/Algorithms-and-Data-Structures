#DFS深度优先搜索+递归
#和之前题目的区别是计数，这里还是要理解递归是每次有返回值了才加法，否则count+=1是跳过的
#递归是先向后算，等着结果，跟第一遍算似的

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return
        steps = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(grid, x, y, m, n):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0
            count = 1
            grid[x][y] = 0
            for i, j in steps:
                count += dfs(grid, x + i, y + j, m, n)
            return count

        result = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result = max(result, dfs(grid, i, j, m, n))
        return result

if __name__ == '__main__':
    s= Solution()
    a = s.numIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
    b = s.numIslands([[0]])
    c = s.numIslands([])
    print(a,b,c)
