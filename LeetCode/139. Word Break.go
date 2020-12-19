// O(Time): s * l, s是字符串长度，l是列表中单词数量
// O(Space): s

/* 完全背包
1 创建了字典查询分割串能否放进背包
2 初始都是大数或者false，但是0位置是true，由实际意义而来
*/

/*
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
*/

func wordBreak(s string, wordDict []string) bool {
	wordSet := make(map[string]bool, len(wordDict))
	for _, word := range wordDict {
		wordSet[word] = true
	}
	dp := make([]bool, len(s)+1)
	dp[0] = true
	for i := 1; i <= len(s); i++ {
		dp[i] = false
	}

	for i := 1; i <= len(s); i++ {
		for _, word := range wordDict {
			// 能放进背包：后面到i的字符串正好等于当前字典中遍历到的单词
			if len(word) <= i && wordSet[s[(i-len(word)):i]] {
				// 判断是否要放进背包
				// 背包问题好像都需要有自己当前值来进行比较，所以有dp[i]
				dp[i] = dp[i] || dp[i-len(word)]
			}
		}
	}
	return dp[len(s)]
}
