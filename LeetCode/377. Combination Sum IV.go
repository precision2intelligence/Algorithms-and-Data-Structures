// O(Time): target * nums
// O(Space): target

/* 明显的完全背包
1 cyc说这是有顺序的完全背包，不理解
2 题目中问什么，dp[i]中就保存什么
3 初始状态赋值可以采用举例法，不易出错
*/

/*
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.


Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

*/

func combinationSum4(nums []int, target int) int {
	dp := make([]int, target+1)
	// 易错：开始的时候，dp[0]要等于1，比如tar是4，nums只有4，dp[tar-num]要跳转到dp[0],需要加1
	dp[0] = 1
	for i := 1; i <= target; i++ {
		for _, num := range nums {
			if num <= i {
				dp[i] += dp[i-num]
			}
		}
	}
	return dp[target]
}