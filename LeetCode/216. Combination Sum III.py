# Time:O(k)，其中 k 为所有可行解的长度之和。比较松的上界是O(9*2^9). 9个位置考虑选还是不选。尽管有排序，nlogn可以忽略
# Space：O(k) 最坏情况递归k层

# 已经排序且无重，不需要visited

'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.
Example 4:

Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.
Example 5:

Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
​​​​​​​There are no other valid combinations.
 

Constraints:

2 <= k <= 9
1 <= n <= 60

'''

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = list()
        # visited = [False for _ in range(9)]
        if k >= n or n > 45:
            return res
        self.backtrack(res, [], n, k, 1)
        return res
    def backtrack(self, res, path, residue, k, begin):
        if residue == 0 and len(path) == k:
            res.append(path)
            return
        if residue < 0 or len(path) > k:
            return
        for i in range(begin, min(residue+1, 10)): # 易错，题目要求小于等于9
            # if visited[i]:
            #     return
            # visited[i] = True
            self.backtrack(res, path + [i], residue - i, k, i+1)
            # visited[i] = False
