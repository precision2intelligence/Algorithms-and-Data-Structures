# Time:O(kCkn) Ckn是构成的组合数，长度为k的组合添加入结果
# Space:O(Ckn)

# 回溯，注意列表中的元素是从1开始的，不是0

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
        res = []
        self.backtrack(res, [], 1, n, k)
        return res
    def backtrack(self, res, path, begin, n, k):
        if len(path) == k:
            res.append(path[:])
        for i in range(begin,n+1):
            path.append(i)
            self.backtrack(res, path, i+1, n, k)
            path.pop()