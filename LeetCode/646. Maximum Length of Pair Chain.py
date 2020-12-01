# Time: O(nlogn)
# Space: O(n)

# 贪心
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # sorted 不会保留排序后的结果
        pairs = sorted(pairs, key=lambda x : x[1])
        cur, ans = float('-inf'), 0
        for x,y in pairs:
            if cur < x:
                cur = y # 很好理解，更新cur用y
                ans += 1
        return ans
