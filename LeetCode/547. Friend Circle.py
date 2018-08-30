#DFS
#N*N的矩阵，只记录人是否是同一个，所以不用二维的visited
#注意里面的self，递归的过程所有地方都要有self,def dfs(self,M...)和self.dfs(...)
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        l = len(M)
        if l == 1:
            return 1
        count = 0
        visited = [0] * l
        for i in range(l):
            if not visited[i]:
                visited[i] = 1
                self.dfs(M,i,visited)
                count += 1
        return count

    def dfs(self,M,i,visited):
        for j in range(len(M)):
            if M[i][j] and not visited[j]:
                visited[j] = 1
                self.dfs(M,j,visited)

M = [[1,1,0],[1,1,0],[0,0,1]]
s = Solution()
print(s.findCircleNum(M))