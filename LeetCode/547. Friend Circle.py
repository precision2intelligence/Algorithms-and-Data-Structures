#DFS
#N*N的矩阵，只记录人是否是同一个，所以不用二维的visited
#注意里面的self，递归的过程所有地方都要有self,def dfs(self,M...)和self.dfs(...)

# There are N students in a class. Some of them are friends, while some are not.
# Their friendship is transitive in nature.
# For example, if A is a direct friend of B, and B is a direct friend of C,
# then A is an indirect friend of C.
# And we defined a friend circle is a group of students who are direct or indirect friends.
#
# Given a N*N matrix M representing the friend relationship between students in the class.
# If M[i][j] = 1, then the ith and jth students are direct friends with each other,
# otherwise not. And you have to output the total number of friend circles among all the students.
#
# Example 1:
# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.
#
# Example 2:
# Input:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
#
# Note:
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.

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