#Time: O(n)
#Space: O(min(m,n))   m is the size of the charset

#思路：动态规划（滑窗）+哈希，和股票买卖类似，只更新最大收益，记住索引
#enumerate简化代码，可以产生（index，item）的遍历，用list可以读取
'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d, res, start = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in d: start = max(start, d[ch] + 1)
            res = max(res, i - start + 1)
            d[ch] = i
        return res
