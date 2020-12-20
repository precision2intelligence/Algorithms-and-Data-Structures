// 考察位运算，16进制是4bit表示一位
// 对比7进制的题，题目要求负数补位处理，如果是负数，也可以用2^32+num进行计算，仍用7进制的取余法
// num != 0 的判断条件，是移位后不为0，这样保证高位为0的情况下不输出前导0

/*
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"

*/

func toHex(num int) string {
	// 后面限制边界：不为0，所以这里处理0的特殊情况
	if num == 0 {
		return "0"
	}
	var numDict = []string{
		"0",
		"1",
		"2",
		"3",
		"4",
		"5",
		"6",
		"7",
		"8",
		"9",
		"a",
		"b",
		"c",
		"d",
		"e",
		"f",
	}
	// 这样写好像会成byte
	//numDict := "123456789abcdef"
	mask := 0xf
	res := ""
	for i := 0; i < 8 && num != 0; i++ {
		res = numDict[num&mask] + res
		num >>= 4
	}
	return res
}
