# 解法一：桶排序
# 同样的，可以用优先队列，参考347题。pq时间复杂度高，因为要统计频率，所有空间复杂度也不低
# Time:  O(n)
# Space: O(n)

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # 统计字母出现的频率
        freq_dic = dict()
        for charac in s:
            freq_dic[charac] = freq_dic.get(charac, 0) + 1

        # 桶排序
        bucket = [[] for _ in range(len(s)+1)]
        for charac, freq in freq_dic.items():
            bucket[freq].append(charac)

        # 逆序返回结果
        res = ''
        for i in range(len(s),-1,-1):
            res += ''.join([charac * i for charac in bucket[i]])
        return res

# 解法二：trick
class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([i*j for i,j in Counter(s).most_common()])