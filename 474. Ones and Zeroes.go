// O(Time)：mn×l, l是字符串个数
// O(Space):mn

// 0-1背包问题，但是背包有了两个体积限制：0和1
/*
1 统计每个字符串的0和1个数，等于直接开始了外层循环
2 之前一直想不明白空间优化如何保证体积减法不越界，这道题明白了，控制了i>zeros的边界
3 边界问题：初始化dp为(m+1)*(n+1),返回dp[m][n],内层循环是有等于0的
4 golang的strings包统计字符
5 golang没有max函数

*/

/*
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.



Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.


Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100

*/

import "strings"

// 没有写统计的函数，因为string包自带了
func findMaxForm(strs []string, m int, n int) int {
	dp := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		dp[i] = make([]int, n+1)
	}
	for _, s := range strs {
		zeros := strings.Count(s, "0")
		ones := len(s) - zeros
		if zeros > m || ones > n {
			continue
		}
		for i := m; i >= zeros; i-- {
			for j := n; j >= ones; j-- {
				dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
			}
		}
	}
	return dp[m][n]
}

func max(m, n int) int {
	if m > n {
		return m
	}
	return n
}


