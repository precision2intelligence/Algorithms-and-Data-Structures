// Time: O(n)
// Space: O(1)
// 数组中的元素最多遍历一次，时间复杂度为 O(N)。只使用了两个额外变量，空间复杂度为 O(1)。

/*
执行用时：4 ms
内存消耗：3 MB
*/

/*
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

*/
func twoSum(numbers []int, target int) []int {
	l, r := 0, len(numbers)-1
	for l < r {
		tmp := numbers[l] + numbers[r]
		if tmp < target {
			l++
		} else if tmp > target {
			r--
		} else {
			return []int{l + 1, r + 1}
		}
	}
	return nil //这里必须有返回
}