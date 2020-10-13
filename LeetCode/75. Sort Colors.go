package main

import "fmt"

// Time: O(n)
// Space: O(1)

// 类似三路快排

/*
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?


Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.
*/

func sortColors(nums []int) {
	red, blue := 0, len(nums)-1
	curr := 0
	for curr <= blue {
		if nums[curr] == 0 {
			nums[red], nums[curr] = nums[curr], nums[red]
			red++
			curr++
		} else if nums[curr] == 2 {
			nums[blue], nums[curr] = nums[curr], nums[blue]
			blue--
		} else {
			curr++
		}
	}

}

func main() {
	fmt.Printf("hello world\n")
	nums := []int{2, 0, 2, 1, 1, 0}
	sortColors(nums)
	fmt.Printf("%p", &nums)
	fmt.Printf("%v", nums)
}
