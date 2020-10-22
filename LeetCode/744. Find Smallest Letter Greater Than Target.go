// Time: O(logn) n是字符串长度
// Space: O(1)

// 有序用二分，二分注意边界

/*
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.

*/

func nextGreatestLetter(letters []byte, target byte) byte {
	lo, hi := 0, len(letters)-1

	for lo <= hi {
		mid := (lo + hi) >> 1
		if letters[mid] <= target {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	find := letters[lo%len(letters)]
	if find <= target {
		find = letters[0]
	}
	return find
}