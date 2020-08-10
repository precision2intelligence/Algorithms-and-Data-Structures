import "math"

// Time: O(sqrt(target))
// Space: O(1)

// 执行用时：0 ms
// 内存消耗：1.9 MB

/*
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5


Example 2:

Input: 3
Output: False

*/

func judgeSquareSum(c int) bool {
	l, r := 0, int(math.Sqrt(float64(c))) //int(math.Sqrt)向下取整，且参数必须为浮点
	for l < r {
		tmp := l*l + r*r
		if tmp < c {
			l++
		} else if tmp > c {
			j--
		} else {
			return true
		}
	}
	return false
}

