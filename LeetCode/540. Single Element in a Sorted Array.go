// Time: O(logn)
// Space: O(1)

// 思路：二分查找 +　只看偶数索引
// 偶数索引与后面相同，则异常数在右侧，左边界右移
// 偶数索引与后面不等，则异常数就是当前或者左侧，右边界左移

/*
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.



Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10


Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
*/

func singleNonDuplicate(nums []int) int {
	l, r := 0, len(nums)-1

	for l < r {
		mid := (l + r) >> 1
		if mid%2 == 1 { // go中if mid % 2 会报错，bool和int不能混用
			mid -= 1
		}
		if nums[mid] == nums[mid+1] { // 这里务必要和后面的比较，因为上面是减1.和前面比较会越界
			l = mid + 2
		} else {
			r = mid
		}
	}
	return nums[l]

}