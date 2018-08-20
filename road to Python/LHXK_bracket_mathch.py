# Time:  O(1)
# Space: O(1)
# Method: 栈

# Note:
# 开始的时候可以先排除一些情况，加快运行。
# 先开的括号必然先闭。
class Solution(object):
    def bracket_mathch(self,str):
        if len(str) % 2 != 0:
            return False
        if len(set(str)) % 2 != 0:
            return False
        bracket_dic = {'}':'{',']':'[',')':'(','》':'《','>':'<'}
        if str[0] in bracket_dic.keys():
            return False
        res = []
        for item in str:
            if item in bracket_dic.values():
                res.append(item)
            elif len(res) != 0:
                if bracket_dic[item] == res[-1]:
                    res.pop()
                else:
                    return False
            else:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    one_str_list = ['({})', '({[<《》>]})', '[(]){}', '{{{{{{', '([{}])', '}{[()]']
    for one_str in one_str_list:
        res = s.bracket_mathch(one_str)
        print(res)