#DFS
#和朋友圈问题的不同，在def下定义的dfs不需要self
#dfs思路是：写主函数需要什么，给一个入口函数；然后再定义这个需求（很多不需要中途返回，只要结尾定义就好，本题就是）
#弄清strings传进来的是同一个

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mpdigits = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(num, strings, res):
            if num == l:
                res.append(strings)
                return
            for letter in mpdigits[digits[num]]:
                dfs(num + 1, strings + letter, res)

        l = len(digits)
        if not len(digits):
            return []
        res = []
        dfs(0, '', res)
        return res
