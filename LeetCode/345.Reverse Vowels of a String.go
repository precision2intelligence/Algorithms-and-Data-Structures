// Time: O(n)
// Space: O(1) 两个变量

/*
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

*/

func reverseVowels(s string) string {
	l, r := 0, len(s)-1
	bytes := []byte(s)
	for l < r {
		for l < r && !isVowels(bytes[l]) { // 限定边界
			l++
		}
		for l < r && !isVowels(bytes[r]) { // 限定边界
			r--
		}
		bytes[l], bytes[r] = bytes[r], bytes[l]
		l++
		r--
	}
	return string(bytes)
}

func isVowels(b byte) bool {
	return b == 'a' || b == 'A' || b == 'e' || b == 'E' || b == 'i' || b == 'I' || b == 'o' || b == 'O' || b == 'u' || b == 'U'
}

