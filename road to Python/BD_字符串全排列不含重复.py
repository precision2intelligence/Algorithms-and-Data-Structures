#解法一是递归，解法二是trick，用了itertools
#解法一用set去重，解法二用判断去重

import itertools

class Solution:
    def Permutation1(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return [ss]
        ret = []
        #遍历字符串，固定第一个元素，然后递归求解
        for i in range(len(ss)):
            for j in self.Permutation1(ss[:i]+ss[i+1:]):#去掉了当前位置的字母再递归
                ret.append(ss[i]+j)
        #通过set进行去重，sorted进行重新排序
        return sorted(list(set(ret)))

    def Permutation2(self, ss):
        # write code here
        result = []
        if not ss:
            return []
        else:
            res = itertools.permutations(ss)
            # print(list(res))#[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
            for i in res:
                if "".join(i) not in result:
                    result.append("".join(i))
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.Permutation1('abs'))
    print(s.Permutation2('xyz'))

'''
['abs', 'asb', 'bas', 'bsa', 'sab', 'sba']
['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx']
'''