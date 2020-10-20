// Time: O(n)
// Space: O(1)

// 难点是下移i（当i-1小于i+1）还是上移i+1（当i-1大于i+1）

/*
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).



Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
*/
func checkPossibility(nums []int) bool {
	var count int

	for i := 0; i < len(nums)-1; i++ {
		if nums[i] > nums[i+1] {
			// 注意等号，注意i==0合并到这里
			if (i > 0 && nums[i-1] <= nums[i+1]) || i == 0 {
				nums[i] = nums[i+1]
			} else {
				nums[i+1] = nums[i]
			}
			// 注意count++的位置
			count++

			if count > 1 {
				return false
			}

		}
	}

	return count <= 1
}