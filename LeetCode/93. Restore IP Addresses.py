'''Given a string containing only digits,
restore it by returning all possible valid IP address combinations.
'''

#dfs
#最关键的是：每次如何保证加上的是少于个数字
#传参3个：待查串、每个的结果暂存、最后的结果
#还是需要借助for来进行边界限制
#判断下一个位置加1,2,3个数字，即使是0，可以在dfs里处理掉

#ps：IP地址不合法的情况：每个点里超过3个数字或没有数字、每个段里如果数字多于1个那么开头不能为0、不能大于255


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s,[],res)
        return res
    def dfs(self,str,path,res):
        if len(str) > 3*(4-len(path)) or (len(path) < 4 and not str):
            return
        elif not str and len(path) == 4:
            res.append('.'.join(path))
            return
        for i in range(min(3,len(str))):#判断下一个位置加1,2,3个数字，即使是0，可以在dfs里处理掉
            curr = str[:i+1] #最关键的一步
            if int(curr) > 255 or (curr[0] == '0' and len(curr) > 1):
                continue
            self.dfs(str[i+1:],path+[str[:i+1]],res)