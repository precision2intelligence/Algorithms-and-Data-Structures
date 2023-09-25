#Time: O(nklog(k) 需要遍历 n 个字符串，对于每个字符串，需要 O(klogk)的时间进行排序以及 O(1)的时间更新哈希表，因此总时间复杂度是 O(nklogk)
#Space: O(nk) 其中 n 是 strs 中的字符串的数量，k 是 strs 中的字符串的的最大长度。

#解法一：排序后存哈希
'''
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

示例 2:
输入: strs = [""]
输出: [[""]]

示例 3:
输入: strs = ["a"]
输出: [["a"]]

提示：
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母
'''
import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_map = collections.defaultdict(list)
        for str in strs:
            k = ''.join(sorted(str))
            str_map[k].append(str)
        return list(str_map.values())

# 解法二：计数后存哈希，省略