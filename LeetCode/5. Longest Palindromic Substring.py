# Given a string s, find the longest palindromic subsequence's length in s.
# You may assume that the maximum length of s is 1000.
#
# Example 1:
# Input:
#
# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input:
#
# "cbbd"
# Output:
# 2

#解法一：
# Time:  O(n^2)
# Space: O(1)
class Solution(object):

    def getlongestpalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1 : r]  # 例如bab，最后l=-1，r=3，所以要s[l+1 : r]也就是[0,3]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindrome = ''
        for i in range(len(s)):
            len1 = len(self.getlongestpalindrome(s, i, i))  # len1是中间是单一字母的回文数
            if len1 > len(palindrome):
                palindrome = self.getlongestpalindrome(s, i, i)
            len2 = len(self.getlongestpalindrome(s, i, i + 1))  # len2是中间是和后面一个字母相同的回文数
            if len2 > len(palindrome):
                palindrome = self.getlongestpalindrome(s, i, i + 1)
        return palindrome


#解法二：
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        maxl = 0
        start = 0
        for i in range(n):
            if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start: start + maxl]