// O(Time): O(logn)
// O(Space): O(1)

/* 递归
1 res = n/5 + n/25 + n/125 + n/625 + …… 都是5的n次方
2 结果要数5的个数，因为2有很多，这样才能凑10，即末尾0
*/

/*
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?



Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0


Constraints:

0 <= n <= 104
*/

func trailingZeroes(n int) int {
	if n != 0 {
		return trailingZeroes(n/5) + n/5
	}
	return 0
}