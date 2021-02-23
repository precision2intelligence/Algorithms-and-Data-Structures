// Time: O(n) 遍历数组
// Space: O(1)

// 动规：当前值f(i) = max(f(i-1)+nums[i], nums[i])
// 最大值：max(f(i), maxNum) maxNum是前面的最大值

/*
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-100000]
Output: -100000
 

Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
*/
func maxSubArray(nums []int) int {
	m := len(nums)
	if m == 1 {
		return nums[0]
	}
	// 解法一：动规，空间复杂度为n，不好想
	// dp, res := make([]int, m), nums[0]
	// dp[0] = nums[0]
	// for i := 1; i < m; i++ {
	// 	if dp[i-1] >= 0 {
	// 		dp[i] = dp[i-1] + nums[i]
	// 	} else {
	// 		dp[i] = nums[i]
	// 	}
	// 	res = max(dp[i], res)

	// 解法二：压缩空间的动规
	res, pre := nums[0], nums[0]
	for i := 1; i < m; i++ {
		pre = max(pre+nums[i], nums[i])
		res = max(pre, res)
	}
	return res
}

func max(a,b int) int{
	if a > b {
		return a
	} else {
		return b
	}
}