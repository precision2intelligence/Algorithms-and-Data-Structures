// Time: O(n)
// Space: O(1)

// 贪心，记录最远位置

/*
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 3 * 104
0 <= nums[i] <= 105

*/
func canJump(nums []int) bool {
	maxPos, m := 0, len(nums)
	// i < m, 不含等于，处理nums=[0]的特殊情况
	for i := 0; i < m; i++ {
		if i <= maxPos {
			maxPos = max(i+nums[i], maxPos)
			if maxPos >= m-1 {
				return true
			}
		}
	}
	return false
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}