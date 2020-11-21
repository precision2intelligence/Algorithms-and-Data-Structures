# Time:O(S)，其中 S 为所有可行解的长度之和。比较松的上界是O(n*2^n). n个位置考虑选还是不选
# Space：O(target) 最坏情况递归target层

'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500

'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = list()
        end = len(candidates)
        self.backtrack(res, [], candidates, target, 0, end)
        return res
    def backtrack(self, res, path, candidates, residue, begin, end):
        if residue == 0:
            res.append(path)
            return
        if residue < 0:
            return
        # 理解逻辑，这里不该减
        # residue = residue - candidates[begin]

        # for item in candidates[begin:end]:
        for index in range(begin, end):
            self.backtrack(res, path+[candidates[index]], candidates, residue - candidates[index], index, end)

