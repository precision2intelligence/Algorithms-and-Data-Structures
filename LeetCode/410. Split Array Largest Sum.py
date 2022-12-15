# Time：O(n×log(sum−maxn))
# Space：O(1)

# 二分法，左边界是数组中的最大值，右边界是数组和，验证函数来决定左右指针如何根据mid调整
# 类似在D天内运输货物的船载重
'''
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= k <= min(50, nums.length)
'''

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = left + ((right-left)>>1)
            need = self.getNeed(nums, mid)
            if need > k:
                left = mid + 1
            elif need < k:
                right = mid - 1
            elif need == k:
                right = mid - 1
        if left > sum(nums): return -1
        if left < max(nums): return max(nums)
        return left
    # 验证函数
    def getNeed(self, nums, mid):
        curr, need = 0, 1
        for num in nums:
            if curr + num > mid:
                need += 1
                curr = 0
            curr += num
        return need