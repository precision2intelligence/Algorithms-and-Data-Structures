// Time: O(logn)
// Space: O(1)

/*
开始先排除一些肯定不在数组内的情况。
陷阱：在首末数字之间但是还是没有

两遍二分找出等于target的第一个数和第二个数
开始务必对l_id,r_id赋值，防止找不到数字，直接返回－１

*/

/*
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
*/
func searchRange(nums []int, target int) []int {
	l, r := -1, -1
	if len(nums) == 0 || nums[len(nums)-1] < target || nums[0] > target {
		return []int{l, r}
	}

	l_id, r_id := -1, -1
	l, r = 0, len(nums)-1
	for l <= r {
		mid := (l + r) >> 1
		if nums[mid] < target {
			l = mid + 1
		} else if nums[mid] > target {
			r = mid - 1
		} else {
			if mid-1 >= 0 && nums[mid-1] == target {
				r = mid - 1
			} else {
				l_id = mid
				break
			}
		}
	}

	l, r = 0, len(nums)-1
	for l <= r {
		mid := (l + r) >> 1
		if nums[mid] < target {
			l = mid + 1
		} else if nums[mid] > target {
			r = mid - 1
		} else {
			if mid+1 < len(nums) && nums[mid+1] == target {
				l = mid + 1
			} else {
				r_id = mid
				break
			}
		}
	}
	return []int{l_id, r_id}
}
