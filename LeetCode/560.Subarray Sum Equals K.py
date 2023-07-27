# Time:O(n)
# Space:O(n)

# 一次遍历取得结果
# 利用前缀和+哈希节约查找时间，利用S(p,q) = S(0,q)-S(0,p)
# 对于python来说，一个if都要简化，不然超时

'''
给你一个整数数组nums和一个整数k ，请你统计并返回该数组中和为k的连续子数组的个数 。

示例1：
输入：nums = [1, 1, 1], k = 2
输出：2

示例2：
输入：nums = [1, 2, 3], k = 3
输出：2

提示：

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
'''

# 简化后
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre_sum = {0:1}
        cur_sum, cnt = 0, 0
        for item in nums:
            cur_sum += item
            cnt += pre_sum.get(cur_sum - k,0)
            pre_sum[cur_sum] = pre_sum.get(cur_sum,0) + 1
        return cnt

# 简化前：思路正确，但是if太多，代码不简洁；利用字典初始化可以减少当前值为答案的判断
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre_sum = {}
        cur_sum = 0
        cnt = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum == k:
                cnt += 1
            if cur_sum - k in pre_sum.keys():
                cnt += pre_sum[cur_sum - k]
            pre_sum[cur_sum] = 1 if cur_sum not in pre_sum.keys() else pre_sum[cur_sum]+1
        return cnt