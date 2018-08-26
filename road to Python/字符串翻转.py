#语法是
#seq[start:end:step]
#range(100)[5:18:2]
#结果是[5, 7, 9, 11, 13, 15, 17]

class Solution():
    def reverse_str(self,str):
        if not str:
            return
        return str[::-1]

s = Solution()
print(s.reverse_str('helloworld'))
