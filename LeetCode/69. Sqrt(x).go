// Time: O(logx)
// Space: O(1)

// 二分法，尤其注意边界

/*
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

*/

func mySqrt(x int) int {
	l, r := 0, x
	ans := -1 // golang特性，先定义在全局再返回，不能直接返回mid
	for l <= r {
		mid := (l + r) / 2
		if mid*mid <= x { // 等号要加上，不然超时，本质还是多更新边界
			ans = mid // ans要及时更新
			l = mid + 1
		} else if mid*mid > x {
			r = mid - 1
		}
	}
	return ans
}
