# Time:O(kCkn) Ckn是构成的组合数，长度为k的组合添加入结果
# Space:O(Ckn)

# 回溯，剪枝为后面的数是下次遍历的上界
# 思路是对的，但是还是比较慢，不知道原因
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
1 <= k <= n

'''

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        visited = [False for _ in range(n)]
        res = list()
        self.backtrack(res, [], 1, k, visited, n)
        return res
    def backtrack(self, res, path, id, k, visited, n): # 这里没有当前数的验证
        if len(path) == k:
            res.append(path)
            return
        for i in range(id, n+1): # 每次都重新遍历
            if visited[i-1]:
                continue
            visited[i-1] = True
            self.backtrack(res, path+[i], i+1, k, visited, n)
            visited[i-1] = False
