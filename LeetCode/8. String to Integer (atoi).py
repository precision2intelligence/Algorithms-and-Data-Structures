'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
'''
#解法一：直接法
#注意，第一个不是数字的就break
#有个转换ASCII的函数ord()很值得注意，判断是不是数字字符的，直接用<,>比较大小就可以

#解法二：
#正则匹配，涉及开头匹配、？非贪婪、+1到多、search比match更实用、group()返回所以符合条件的对象、group()支持索引
#try和except搭配使用
class Solution(object):
    def myAtoi1(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str or not str.strip():
            return 0
        num, flag = 0, 1
        str = str.strip()
        if str[0] == '-':
            flag = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        for item in str:
            if item >= '0' and item <= '9':
                num = 10*num + ord(item) - ord('0')
            else:
                break
        num = num * flag
        if num > 2147483647:
            return 2147483647
        elif num < -2147483647:
            return -2147483648
        return num

    def myAtoi1(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        try:
            str = re.search('^[+-]?\d+', str).group()
            res = int(str)
            if res >= 0:
                res = min(res, 2147483647)
            else:
                res = max(res, -2147483648)
        except:
            res = 0
        return res