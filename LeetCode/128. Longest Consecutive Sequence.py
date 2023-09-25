#Time: O(n)
#Space: O(n)

# 思路：set去重等于字典查找的O(1)复杂度
# 判断当前数字是否是最小的数，如是，则开始遍历取连续值，作为中间状态最大值；如果不是，就跳过不看了，这样保证只有最小值才进行遍历。有几个最小值就遍历几次，k*n
'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9


提示：
0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                cur_num = num
                cur_streak = 1
                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_streak += 1
                longest_streak = max(longest_streak, cur_streak)
        return longest_streak