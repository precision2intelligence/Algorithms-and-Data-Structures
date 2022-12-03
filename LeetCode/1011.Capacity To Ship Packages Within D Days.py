# Time：O(nlog(Σw)) 二分查找时间复杂度是log(Σw)，在验证函数里，每个货船重量都要遍历一次数组
# Space：O(1)
'''
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

 

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
Example 2:

Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:

Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
 

Constraints:

1 <= days <= weights.length <= 5 * 104
1 <= weights[i] <= 500

'''

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = left + ((right - left) >> 1)
            # 单独一个函数验证是否能在days天内运走全部货物
            flag = self.valid(weights, mid, days)
            if flag:
                right = mid - 1
            else:
                left = mid + 1
        if left > sum(weights): return sum(weights)
        if left < max(weights): return max(weights)
        return left

    def valid(self, weights, mid, days):
        cnt, curr = 1, 0
        for item in weights:
            if curr + item <= mid:
                curr += item
            else:
                cnt += 1
                curr = item
        return True if cnt <= days else False