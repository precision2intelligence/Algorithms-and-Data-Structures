# Time:O(S)，其中 S 为所有可行解的长度之和。比较松的上界是O(n*2^n). n个位置考虑选还是不选。尽管有排序，nlogn可以忽略
# Space：O(target) 最坏情况递归target层

'''
聪明的剪枝：
1. 先对数组排序
2. 每次回溯只保留小于残差的数字组成列表，因为排序过，所以visited和索引不变
3. 回溯时限定begin，为了不超过len(candidate)，回溯时送入的begin=i，但是i会在最开始校验visited时被抛弃
'''

'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

'''



class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        visited = [False for _ in range(len(candidates))]
        res = list()
        candidates.sort()
        self.backtrack(res, [], candidates, target, visited,0)
        return res
    def backtrack(self, res, path, candidates, residue, visited, start):
        if residue == 0:
            res.append(path)
            return
        if residue < 0:
            return
        candidates = [x for x in candidates if x <= residue]
        for i in range(start, len(candidates)):
            if visited[i]:
                continue
            if i>0 and candidates[i-1] == candidates[i] and not visited[i-1]:
                continue
            visited[i] = True
            self.backtrack(res, path + [candidates[i]], candidates, residue - candidates[i], visited, i)
            visited[i] = False
