// Time: O(n)
// Space: O(1)

// 运行时间：2ms

// 占用内存：1044k

/*
牛客上要求索引顺序递增。

Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

*/

// 如果字符串有序，则双指针。167题

func twoSum(numbers []int, target int) []int {
	hash := make(map[int]int, len(numbers))
	for k, v := range numbers {
		if idx, ok := hash[target-v]; ok { //golang字典检索用新变量
			return []int{idx + 1, k + 1}
		}
		hash[v] = k
	}
	return nil
}