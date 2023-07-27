# Time：O(n×log(maxn))
# Space：O(1)

# 二分查找，左边界是吃1根，右边界是数组中的最大值。这道题没有复杂的验证函数，因为不会同时吃两堆香蕉
'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = left + ((right-left)>>1)
            curr, need = 0, 0
            for pile in piles:
                need += ceil(pile / mid)
            if need > h:
                left = mid + 1
            elif need < h:
                right = mid - 1
            elif need == h:
                right = mid - 1
        if left > max(piles): return max(piles)
        if left < 1 : return 1
        return left