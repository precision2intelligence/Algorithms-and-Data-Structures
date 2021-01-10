// Time: O(n)
// Space: O(1)

// 贪心，记录最远位置.注意步数是截止到最后位置之前的

/*
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 3 * 104
0 <= nums[i] <= 105
*/

func jump(nums []int) int {
	maxPos, m := 0, len(nums)
	step := 0
	end := 0
	// i < m-1 跳到最后一步不用跳了
	for i := 0; i < m-1; i++ {
		if i <= maxPos {
			maxPos = max(i+nums[i], maxPos)
		}
		if i == end {
			end = maxPos
			step++
		}
	}
	return step
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}