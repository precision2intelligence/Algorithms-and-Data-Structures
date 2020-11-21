# Time：O(n*n!)
# Space:O(n) 递归深度，等于数组长度

# 回溯法
# 最难的是不进入的条件，前面的数字已经释放，同时还和之前的相等，并列关系，即不用进入了，和重复几次没有关系；但是前一个数没有被释放，就需要进入回溯
# 注意append, remove, insert 都没有返回值，但是改变了原数组，这一次用加号

'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
'''

class Solution:
    def permuteUnique(self, nums):
        visited = [False for _ in range(len(nums))]
        nums.sort()
        res = list()
        # 同一个类内，无论函数是否是调用自己，都加self
        self.backtrack(res,[],nums,visited)
        return res
    def backtrack(self, res, path, nums,visited):
        if len(path) == len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            visited[i] = True
            ## !!! 易错
            # path.append之后，可以进入回溯，但是在回溯退出的时候，path已经改变了，即一条完整的len(nums)长的路径
            # path + [nums[i]],注意，两个中括号。在加后返回列表，但是path的值没有改变。所以能在每一次回溯的时候得到空的列表
            # path.append(nums[i])
            self.backtrack(res, path+[nums[i]], nums, visited)
            visited[i] = False
