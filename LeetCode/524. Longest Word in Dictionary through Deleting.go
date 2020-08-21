// 思路：双指针
// Time : O(n*l), n 为dictionary大小，l 是string的长度
// Space : O(1)

// 另有一种解法：先字典排序，再判断是否是子串。
// Time : O(nlogn + n*l)
// Space : O(logn) 排序空间复杂度

/*
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
*/

func findLongestWord(s string, d []string) string {
	res := ""
	for _, substr := range d { // 类似python的enumerate
		if isSubstr(s, substr) && (len(substr) > len(res) || (len(substr) == len(res) && res > substr)) { // go、py中字符串可以直接比大小。按照Unicode逐个字母比较
			res = substr
		}
	}
	return res
}

func isSubstr(s string, substr string) bool {
	i, j := 0, 0
	for i < len(s) && j < len(substr) {
		if s[i] == substr[j] {
			j++
		}
		i++
	}
	if j == len(substr) {
		return true
	} else {
		return false
	}
}