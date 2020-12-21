// 递归

/*
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
*/

// 26进制转换，但是每个位置都有坑
func convertToTitle(n int) string {
	// 1~26都要进这个循环，而且A是第一个数，Z是第26个数
	// n-1,因为起始位置是A
	if n <= 26 {
		return string('A' + (n-1)%26)
	}
	// 递归除数和余数
	// 除数：要减1再取，因为52不能是B，而是AZ
	// 余数：先减1再加1，比如52，直接取余数是0，但是满26就要新有一位，所以先减1取余25，再加1
	return convertToTitle((n-1)/26) + convertToTitle((n-1)%26+1)
}