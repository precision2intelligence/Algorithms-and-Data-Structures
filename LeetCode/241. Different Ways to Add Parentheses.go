// Time: O(3^n)
// Space: O(3^n)

// 算法思想是分治，复杂度高

/*
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
*/
import (
	"strconv"
)

func diffWaysToCompute(input string) []int {
	// 后面用到了res，这里还用res命名会报重复命名的错误
	re, err := strconv.Atoi(input)
	if err == nil {
		return []int{re}
	}

	var res []int
	for index, c := range input {
		tmpC := string(c)
		if tmpC == "+" || tmpC == "-" || tmpC == "*" {
			left := diffWaysToCompute(input[:index]) // 没有self，可以直接用
			right := diffWaysToCompute(input[index+1:])

			// var newNum int
			for _, l := range left { // i,l 遍历range不可以，因为i后面没用到
				for _, r := range right {
					var newNum int
					if tmpC == "+" {
						newNum = l + r
					} else if tmpC == "-" {
						newNum = l - r
					} else {
						newNum = l * r
					}
					res = append(res, newNum)
				}
			}
		}
	}
	return res
}
