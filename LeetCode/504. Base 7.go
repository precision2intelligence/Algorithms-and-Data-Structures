// 递归
// 注意负号的处理
// golang 除法向0取整，python 向负无穷取整

/*
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].

*/

import "strconv"

func convertToBase7(num int) string {
	if num == 0 {
		return "0"
	}
	if num < 0 {
		return "-" + dfs(-num)
	}
	return dfs(num)
}

func dfs(num int) string {
	if num == 0 {
		return ""
	}
	return dfs(num/7) + strconv.Itoa(num%7)
	// import "fmt"
	// return dfs(num/7) + fmt.Sprintf("%d", num%7)
}