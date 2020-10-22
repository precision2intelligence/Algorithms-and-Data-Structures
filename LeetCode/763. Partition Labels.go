// Time: O(n) 遍历两遍，第一遍统计末端位置，第二遍计算
// Space: O(∑) 这里是26个字母，所以是26

// 易错逻辑，if那里，注意更新end和start，golang的range用法和python不同

/*
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.



Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.


Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.

*/

func partitionLabels(s string) (partition []int) {
	Pos := [26]int{}
	for i, c := range S {
		Pos[c-'a'] = i
	}

	start, end := 0, 0
	partition := []int{}
	for i, c := range S {
		if Pos[c-'a'] > end {
			end = Pos[c-'a'] // i
		}
		if i == end {
			partition = append(partition, end-start+1)
			start = end + 1
		}
	}
	return partition
}