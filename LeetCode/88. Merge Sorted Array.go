// Time : O(m+n)
// Space : O(1) 原地排序，还是nums1的空间大小

// 此题简单，但是有很多坑：1、为了避免空间复杂度高，要原地规定到nums1; 2、题意是把结果合并到nums1里，所以没有返回值；3、m代表nums1中要用的是前m个数字排序;4、不同于归并，用倒排序

/*
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
*/

func merge(nums1 []int, m int, nums2 []int, n int) {
	if m == 0 {
		copy(nums1, nums2)
		return
	}
	i, j := m-1, n-1
	k := m + n - 1
	for ; i >= 0 && j >= 0; k-- {
		if nums1[i] < nums2[j] {
			nums1[k] = nums2[j]
			j--
		} else {
			nums1[k] = nums1[i]
			i--
		}
	}
	for ; j >= 0; k-- {
		nums1[k] = nums2[j]
		j--
	}
	return
}