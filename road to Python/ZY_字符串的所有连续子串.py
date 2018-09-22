#题目：找出字符串的所有连续子串

#解法一：一行搞定
s = 'abcdef'
res = [s[i:i + x + 1] for x in range(len(s)) for i in range(len(s) - x)]
print(res)

#解法二：解法一的展开版本
def cut(s: str):
    results = []
    # x + 1 表示子字符串长度
    for x in range(len(s)):
        # i 表示偏移量
        for i in range(len(s) - x):#边界
            results.append(s[i:i + x + 1])
    return results

print(cut('abcdef'))



