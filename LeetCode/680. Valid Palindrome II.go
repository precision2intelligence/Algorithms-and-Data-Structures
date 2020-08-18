// Time : O(n)
// Space : O(1)

// 易错点：找不到返回false的情况：只要有一次减少了字母，之后再有不相等，就要返回false；
// 善用辅助函数

/*
执行用时：20 ms
内存消耗：6.4 MB
*/

/*
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
*/

func validPalindrome(s string) bool {
	if len(s) == 0 || len(s) == 1 {
		return true
	} else {
		l, r := 0, len(s)-1
		bytes := []byte(s)
		for l < r {
			if bytes[l] == bytes[r] {
				l++
				r--
			} else {
				return isPalindrome(bytes, l+1, r) || isPalindrome(bytes, l, r-1)
			}
		}
		return true
	}

}
func isPalindrome(sub []byte, i, j int) bool {
	for i < j {
		if sub[i] == sub[j] {
			i++
			j--
		} else {
			return false
		}
	}
	return true
}
