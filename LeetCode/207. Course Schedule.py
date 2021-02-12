'''
Time：O(E + V),这里 E 表示邻边的条数，V 表示结点的个数。初始化入度为 0 的集合需要遍历整张图，具体做法是检查每个结点和每条边，因此复杂度为 O(E+V)，然后对该集合进行操作，又需要遍历整张图中的每个结点和每条边，复杂度也为 O(E+V)；

Space：O(E + V)：邻接表长度是 V，每个课程里又保存了它所有的边。

'''
# 宽度优先搜索，题解中有个图很好

'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

'''

from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        prelen = len(prerequisites)
        if not prelen:
            return True

        # 入度字典，每个索引的入度
        in_degree = [0 for _ in range(numCourses)]
        # 邻接字典，用set去重
        adj = [set() for _ in range(numCourses)]

        # 课程依赖关系，key为依赖，value（集合内容）为依赖该课程的所有课程
        for cur, pre in prerequisites:
            in_degree[cur] += 1
            adj[pre].add(cur)

        # 不是原生Queue，但是用法
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        # 用计数的方式判断是否遍历了所有课程
        counter = 0
        while queue:
            top = queue.pop()
            counter += 1
            for successor in adj[top]:
                in_degree[successor] -= 1
                if in_degree[successor] == 0:
                    # 注意这里加入的是successor
                    queue.append(successor)

        return counter == numCourses
